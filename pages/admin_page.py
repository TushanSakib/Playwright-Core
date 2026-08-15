import allure

from playwright.sync_api import Page
from playwright.sync_api import expect


class AdminPage:
    PAGE_HEADER = "h6"

    ADD_BUTTON = "//button[normalize-space()='Add']"

    USER_ROLE_DROPDOWN = (
        "(//div[contains(@class,'oxd-select-text')])[1]"
    )

    EMPLOYEE_NAME = (
        "//input[@placeholder='Type for hints...']"
    )

    STATUS_DROPDOWN = (
        "(//div[contains(@class,'oxd-select-text')])[2]"
    )

    USERNAME = (
        "(//input[contains(@class,'oxd-input')])[2]"
    )

    PASSWORD = (
        "(//input[@type='password'])[1]"
    )

    CONFIRM_PASSWORD = (
        "(//input[@type='password'])[2]"
    )

    SAVE_BUTTON = (
        "//button[@type='submit']"
    )

    SUCCESS_TOAST = (
        "//p[contains(@class,'oxd-text--toast-message')]"
    )

    def __init__(self, page: Page):
        self.page = page

    @allure.step("Verify Admin Page Loaded")
    def verify_page_loaded(self):
        expect(
            self.page.locator(self.PAGE_HEADER)
        ).to_have_text("Admin")

    @allure.step("Open Add User Form")
    def open_add_user(self):
        self.page.locator(
            self.ADD_BUTTON
        ).click()

    @allure.step("Create New User")
    def create_user(
            self,
            employee_name,
            username,
            password
    ):
        # User Role
        self.page.locator(
            self.USER_ROLE_DROPDOWN
        ).click()

        self.page.keyboard.press("ArrowDown")
        self.page.keyboard.press("Enter")

        # Employee
        self.page.locator(
            self.EMPLOYEE_NAME
        ).fill(employee_name)

        self.page.wait_for_timeout(2000)

        self.page.keyboard.press("ArrowDown")
        self.page.keyboard.press("Enter")

        # Status
        self.page.locator(
            self.STATUS_DROPDOWN
        ).click()

        self.page.keyboard.press("ArrowDown")
        self.page.keyboard.press("Enter")

        self.page.locator(
            self.USERNAME
        ).fill(username)

        self.page.locator(
            self.PASSWORD
        ).fill(password)

        self.page.locator(
