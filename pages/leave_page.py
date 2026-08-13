import allure
from playwright.sync_api import Page, expect


class LeavePage:

    PAGE_HEADER = "h6"

    ASSIGN_LEAVE_MENU = (
        "//a[text()='Assign Leave']"
    )

    EMPLOYEE_NAME = (
        "//input[@placeholder='Type for hints...']"
    )

    LEAVE_TYPE_DROPDOWN = (
        "(//div[contains(@class,'oxd-select-text')])[1]"
    )

    FROM_DATE = (
        "(//input[@placeholder='yyyy-dd-mm'])[1]"
    )

    TO_DATE = (
        "(//input[@placeholder='yyyy-dd-mm'])[2]"
    )

    COMMENT = "testarea"

    ASSIGN_BUTTON = (
        "//button[@type='submit']"
    )

    SUCCESS_TOAST = (
        "//p[contains(@class,'oxd-text--toast-message')]"
    )

    def __init__(self,page:Page):
        self.page  =page


    @allure.step("Verify Leave Page Loaded")
    def verify_page_loaded(self):
        expect(
            self.page.locator(self.PAGE_HEADER)
        ).to_have_text("Leave")
