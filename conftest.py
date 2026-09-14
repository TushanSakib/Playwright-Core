import os
import time
import re

import allure
import pytest
from playwright.sync_api import sync_playwright

from pages.login_page import LoginPage
from utilities.credential_manage import CredentialManager
from utilities.network_monitor import NetworkMonitor

BASE_URL = (
    "https://opensource-demo.orangehrmlive.com/"
    "web/index.php/auth/login"
)


# Defaults for flaky marker
DEFAULT_RERUNS = 2
DEFAULT_RERUNS_DELAY = 1.0


@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as playwright:
        yield playwright


@pytest.fixture(scope="session")
def browser(playwright_instance):

    browser = playwright_instance.chromium.launch(
        headless=False,
        slow_mo=500
    )

    yield browser

    browser.close()


@pytest.fixture()
def login_as(browser):
    """
    Role based login fixture
    Example:
        page = login_as("admin")
    """

    def _login(role: str):

        credentials = (
            CredentialManager.get_credentials(role)
        )

        context = browser.new_context()

        page = context.new_page()

        page.goto(BASE_URL)

        login_page = LoginPage(page)

        login_page.login(
            credentials["username"],
            credentials["password"]
        )

        page.wait_for_url(
            "**/dashboard/index"
        )

        return page

    return _login


@pytest.fixture()
def logged_in_page(login_as,request):
    """
    Default login as Admin.
    """

    page = login_as("admin")
    context = page.context
    context.tracing.start(
        screenshots=True,
        snapshots=True,
        sources=True
    )

    yield page


def _is_retryable_exception(exc: BaseException) -> bool:
    """Heuristic to detect transient failures worth retrying."""
    if exc is None:
        return False
    msg = str(exc).lower()
    retry_signals = [
        "timeout",
        "timed out",
        "connection reset",
        "temporarily unavailable",
        "resource temporarily unavailable",
        "read timed out",
        "connection aborted",
        "broken pipe",
        "service unavailable",
        "try again",
    ]
    return any(s in msg for s in retry_signals)


def pytest_configure(config):
    # register marker so pytest doesn't warn
    config.addinivalue_line(
        "markers",
        "flaky(reruns=int, reruns_delay=float): mark test as flaky and rerun on failure"
    )


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    setattr(
        item,
        f"rep_{report.when}",
        report
    )


@pytest.fixture(autouse=True)
def capture_screenshot(request):

    yield

    page = request.node.funcargs.get(
        "logged_in_page"
    )

    if not page:
        return

    screenshots_dir = (
        "reports/screenshots"
    )

    os.makedirs(
        screenshots_dir,
        exist_ok=True
    )

    test_name = request.node.name
    attempt = getattr(
        request.node,
        "current_retry_attempt",
        11
    )

    try:

        if getattr(request.node, "rep_call", None) and request.node.rep_call.passed:

            screenshot_path = (
                f"{screenshots_dir}/",
                f"{test_name}_attempt_{attempt}.png"
            )

            page.screenshot(
                path=screenshot_path,
                full_page=True
            )

            allure.attach.file(
                screenshot_path,
                name=(
                    f"{test_name} "
                    f"Attempt-{attempt} PASS"
                ),
                attachment_type=allure.attachment_type.PNG
            )

        elif getattr(request.node, "rep_call", None) and request.node.rep_call.failed:

            screenshot_path = (
                f"{screenshots_dir}/"
                f"{test_name}_attempt_"
                f"{attempt}_FAIL.png"
            )

            page.screenshot(
                path=screenshot_path,
                full_page=True
            )

            allure.attach.file(
                screenshot_path,
                name=(
                    f"{test_name} "
                    f"Attempt-{attempt} FAIL"
                ),
                attachment_type=allure.attachment_type.PNG
            )

    except Exception as e:

        print(
            f"Screenshot capture failed: {e}"
        )


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_call(item):
    """Wrap test execution to retry only when the test is marked with @pytest.mark.flaky.

    Usage:
        @pytest.mark.flaky(reruns=2, reruns_delay=1)
        def test_xxx():
            ...

    If marker is not present, behavior is unchanged.
    """
    marker = item.get_closest_marker("flaky")
    if not marker:
        # default behavior: run once
        outcome = yield
        return

    # marker may provide reruns and reruns_delay
    reruns = None
    reruns_delay = None
    try:
        reruns = marker.kwargs.get("reruns") if marker.kwargs else None
        reruns_delay = marker.kwargs.get("reruns_delay") if marker.kwargs else None
    except Exception:
        # old-style usage: marker.args may be used; ignore
        pass

    if reruns is None:
        # allow marker like @pytest.mark.flaky(3)
        if marker.args:
            try:
                reruns = int(marker.args[0])
            except Exception:
                reruns = DEFAULT_RERUNS
        else:
            reruns = DEFAULT_RERUNS

    if reruns_delay is None:
        if marker.args and len(marker.args) > 1:
            try:
                reruns_delay = float(marker.args[1])
            except Exception:
                reruns_delay = DEFAULT_RERUNS_DELAY
        else:
            reruns_delay = DEFAULT_RERUNS_DELAY

    attempts = 0
    last_exc = None

    while attempts <= reruns:
        attempts += 1
        item.current_retry_attempt = attempts
        start = time.perf_counter()
        outcome = yield
        # after the yield, pytest has executed the test and populated reports
        rep_call = getattr(item, "rep_call", None)

        duration = time.perf_counter() - start

        if rep_call and rep_call.passed:
            # success — nothing to do
            return

        # test failed
        # capture exception from the report if available
        exc = None
        if rep_call and hasattr(rep_call, "longrepr"):
            # longrepr can be various types; try to extract message
            try:
                longrepr = rep_call.longrepr
                if hasattr(longrepr, "reprcrash"):
                    exc = getattr(longrepr, "reprcrash").message
                else:
                    exc = str(longrepr)
            except Exception:
                exc = None

        # decide whether to retry: for marker-based flaky tests, always retry unless last attempt
        if attempts > reruns:
            # no more retries left
            if rep_call and rep_call.failed:
                # re-raise the failure by returning normally (pytest will report it)
                return
            return

        # optional: only retry immediately if exception looks transient or test was slow
        retryable = _is_retryable_exception(exc)
        slow_threshold = 10.0  # seconds; conservative
        slow = duration >= slow_threshold

        # For explicit flaky marker, prefer retrying always — but print reason
        reason = "failure"
        if retryable:
            reason = "transient failure"
        elif slow:
            reason = "slow execution"

        print(f"\n[flaky-retry] {item.nodeid} failed ({reason}) after {duration:.2f}s — retry {attempts}/{reruns}")

        # wait before next attempt
        try:
            time.sleep(reruns_delay)
        except Exception:
            pass

        # clear previous reports so next run's reports replace them
        for attr in ("rep_setup", "rep_call", "rep_teardown"):
            if hasattr(item, attr):
                delattr(item, attr)

    # if loop exits normally, let pytest handle final failure

    @pytest.fixture
    def network_monitor(logged_in_page):
        monitor = NetworkMonitor(logged_in_page)
        monitor.start_monitoring()
        return monitor