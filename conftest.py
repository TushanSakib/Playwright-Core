import os

import allure
import pytest
from playwright.sync_api import sync_playwright

from pages.login_page import LoginPage
from utilities.credential_manage import CredentialManager


BASE_URL = (
    "https://opensource-demo.orangehrmlive.com/"
    "web/index.php/auth/login"
)


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
def logged_in_page(login_as):
    """
    Default login as Admin.
    """

    return login_as("admin")


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

    try:

        if request.node.rep_call.passed:

            screenshot_path = (
                f"{screenshots_dir}/"
                f"{test_name}_PASS.png"
            )

            page.screenshot(
                path=screenshot_path,
                full_page=True
            )

            allure.attach.file(
                screenshot_path,
                name=f"{test_name} - PASS",
                attachment_type=allure.attachment_type.PNG
            )

        elif request.node.rep_call.failed:

            screenshot_path = (
                f"{screenshots_dir}/"
                f"{test_name}_FAIL.png"
            )

            page.screenshot(
                path=screenshot_path,
                full_page=True
            )

            allure.attach.file(
                screenshot_path,
                name=f"{test_name} - FAIL",
                attachment_type=allure.attachment_type.PNG
            )

    except Exception as e:

        print(
            f"Screenshot capture failed: {e}"
        )