import allure
from playwright.sync_api import expect, Page


class AdminPage:

    PAGE_HEADER = "h6"

    def __init__(self,page:Page):
        self.page = page

    @allure.step("Verify Admin page loaded")
    def verify_page_loaded(self)->None:
        expect(
            self.page.locator(self.PAGE_HEADER)
        ).to_have_test("Admin")