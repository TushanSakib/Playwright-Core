import allure
import pytest

from playwright.sync_api import Playwright
from playwright.sync_api import Page
from playwright.sync_api import Browser
from playwright.sync_api import BrowserContext
from playwright.sync_api import sync_playwright

from pages.login_page import LoginPage
from utilities.config_reader import ConfigReader


BASE_URL = ("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
USERNAME = "Admin"
PASSWORD = "admin123"

@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as playwright:
        yield playwright


@pytest.fixture(scope="session")
def browser(playwright_instance: Playwright) -> Browser:
    browser_name = ConfigReader.get("browser", "browser_name")
    headless = ConfigReader.get("browser", "headless")
    slow_mo = ConfigReader.get("browser", "slow_mo")

    browser = getattr(playwright_instance, browser_name).launch(
        headless=headless,
        slow_mo=slow_mo
    )

    yield browser

    browser.close()


@pytest.fixture(scope="function")
def context(browser: Browser) -> BrowserContext:
    context = browser.new_context()

    yield context

    context.close()


@pytest.fixture(scope="function")
def page(context: BrowserContext) -> Page:
    page = context.new_page()

    page.set_default_timeout(
        ConfigReader.get("timeouts", "element_timeout")
    )

    yield page

    page.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    setattr(item, "rep_" + report.when, report)


@pytest.fixture(autouse=True)
def screenshot_on_failure(request, page):
    yield

    if request.node.rep_call.failed:

        screenshot = page.screenshot(full_page=True)

        allure.attach(
            screenshot,
            name="Failure Screenshot",
            attachment_type=allure.attachment_type.PNG
        )

@pytest.fixture()
def logged_in_page(browser):
    context = browser.new_context(storage_state="storage_state.json")
    page = context.new_page()
    yield page
    context.close()