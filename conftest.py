import os

import allure
import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as playwright:
        yield playwright


@pytest.fixture(scope="session")
def browser(playwright_instance):

    browser = playwright_instance.chromium.launch(
        headless=False
    )

    yield browser

    browser.close()


@pytest.fixture()
def logged_in_page(browser):

    context = browser.new_context(
        storage_state="storage_state.json"
    )

    page = context.new_page()

    page.goto(
        "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
    )

    yield page

    context.close()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item,call):
    outcome = yield
    report = outcome.get_result()

    setattr(item, f"rep_{report.when}",report)


@pytest.fixture(autouse=True)
def capture_screenshot(request, page):
    yield

    screenshots_dir = "reports/screenshots"
    os.makedirs(screenshots_dir, exist_ok=True)

    test_name = request.node.name

    if request.node.rep_call.passed:

        screenshot_path = (
            f"{screenshots_dir}/{test_name}_PASS.png"
        )

        page.screenshot(
            path=screenshot_path,
            full_page=True,
            timeout=30000
        )

        allure.attach.file(
            screenshot_path,
            name=f"{test_name} - PASS",
            attachment_type=allure.attachment_type.PNG
        )

    elif request.node.rep_call.failed:

        screenshot_path = (
            f"{screenshots_dir}/{test_name}_FAIL.png"
        )

        page.screenshot(
            path=screenshot_path,
            full_page=True,
            timeout=30000
        )

        allure.attach.file(
            screenshot_path,
            name=f"{test_name} - FAIL",
            attachment_type=allure.attachment_type.PNG
        )




