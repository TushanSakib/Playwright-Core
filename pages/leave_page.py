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

    @allure.step("Open assign Leave")
    def open_assign_leave(self):
        self.page.locator(
            self.ASSIGN_LEAVE_MENU
        ).click()

    @allure.step("Assign Leave")
    def assign_leave(self,
                     employee_name,
                     from_date,
                     to_date,
                     comment):
        self.page.locator(
            self.EMPLOYEE_NAME
        ).fill(employee_name)
        self.page.wait_for_timeout(2000)

        self.page.keyboard.press("ArrowDown")

        self.page.keyboard.press("Enter")

        self.page.locator(
            self.LEAVE_TYPE_DROPDOWN
        ).click()

        self.page.keyboard.press(
            "ArrowDown"
        )

        self.page.keyboard.press(
            "Enter"
        )

        self.page.locator(
            self.FROM_DATE
        ).fill(from_date)

        self.page.locator(
            self.TO_DATE
        ).fill(to_date)

        self.page.locator(
            self.COMMENT
        ).fill(comment)

        self.page.locator(
            self.ASSIGN_BUTTON
        ).click()

    @allure.step("Verify leave assigned successfully")
    def verify_leave_assigned(self):
        expect(
            self.page.locator(
                self.SUCCESS_TOAST
            )
        ).to_be_visible()
