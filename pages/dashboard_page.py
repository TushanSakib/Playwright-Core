from playwright.sync_api import Page, expect
import allure


class DashboardPage:
    """
    Dashboard page object.
    Contains dashboard related actions and validations.
    """

    DASHBOARD_TITLE = "h6.oxd-text--h6"

    def __init__(self, page: Page):
        self.page = page

    @allure.step("Verify dashboard page is loaded")
    def verify_page_loaded(self) -> None:
        expect(
            self.page.locator(self.DASHBOARD_TITLE)
        ).to_have_text("Dashboard")

    @allure.step("Get dashboard page title")
    def get_page_title(self) -> str:
        return self.page.locator(
            self.DASHBOARD_TITLE
        ).text_content()