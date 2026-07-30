import allure

from playwright.sync_api import expect

from pages.base_page import BasePage


class DashboardPage(BasePage):

    HEADER = "h6.oxd-text--h6"

    @allure.step(
        "Verify Dashboard Page Loaded"
    )
    def verify_page_loaded(self):

        expect(
            self.page.locator(self.HEADER)
        ).to_have_text(
            "Dashboard"
        )