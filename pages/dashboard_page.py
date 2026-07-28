from playwright.sync_api import expect


class DashboardPage:

    DASHBOARD_HEADER = "//h6[text()='Dashboard']"

    def __init__(self, page):
        self.page = page

    def verify_dashboard_loaded(self):

        expect(
            self.page.locator(self.DASHBOARD_HEADER)
        ).to_be_visible()
