import allure
from playwright.sync_api import Page, expect


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
    SEARCH_USERNAME = (
        "(//input[contains(@class,'oxd-input')])[2]"
    )

    SEARCH_BUTTON = (
        "//button[@type='submit']"
    )

    RESET_BUTTON = (
        "//button[normalize-space()='Reset']"
    )

    RESULT_TABLE = (
        ".oxd-table-body"
    )
    EDIT_BUTTON = (
        "(//i[contains(@class,'bi-pencil-fill')])[1]"
    )
    DELETE_BUTTON = (
        "(//i[contains(@class,'bi-trash')])[1]"
    )
    CONFIRM_DELETE_BUTTON = (
        "//button[normalize-space()='Yes, Delete']"
    )
    NO_RECORD_FOUND = (
        "//span[text()='No Records Found']"
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
        employee_name: str,
        username: str,
        password: str
    ):

        # User Role
        self.page.locator(
            self.USER_ROLE_DROPDOWN
        ).click()

        self.page.keyboard.press("ArrowDown")
        self.page.keyboard.press("Enter")

        # Employee Name
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

        # Username
        self.page.locator(
            self.USERNAME
        ).fill(username)

        # Password
        self.page.locator(
            self.PASSWORD
        ).fill(password)

        # Confirm Password
        self.page.locator(
            self.CONFIRM_PASSWORD
        ).fill(password)

        # Save
        self.page.locator(
            self.SAVE_BUTTON
        ).click()

    @allure.step("Verify User Created Successfully")
    def verify_user_created(self):

        expect(
            self.page.locator(
                self.SUCCESS_TOAST
            )
        ).to_be_visible(timeout=10000)


    @allure.step("Search user: {username}")
    def search_user(self,username:str):
        self.page.locator(
            self.SEARCH_USERNAME
        ).fill(username)

        self.page.locator(
            self.SEARCH_BUTTON
        ).click()

    @allure.step("Verify user found is search")
    def verify_user_found(self,username:str):

        expect(
            self.page.locator(self.RESULT_TABLE)
        ).to_contain_text(username)

    @allure.step("Open user for editing")
    def open_user_for_edit(self):
        self.page.locator(
            self.EDIT_BUTTON
        ).click()

    @allure.step("Update user status")
    def update_user_status(self):
        self.page.locator(
            self.STATUS_DROPDOWN
        ).click()

        self.page.keyboard.press(
            "ArrowDown"
        )
        self.page.keyboard.press(
            "Enter"
        )

        self.page.locator(
            self.SAVE_BUTTON
        ).click()

    @allure.step("Verify user updated successfully")
    def verify_user_updated(self):
        expect(
            self.page.locator(
                self.SUCCESS_TOAST
            )
        ).to_be_visible()

    @allure.step("Delete User")
    def delete_user(self):
        self.page.locator(
            self.DELETE_BUTTON
        ).click()

        self.page.locator(
            self.CONFIRM_DELETE_BUTTON
        ).click()


    @allure.step("Verify user deleted successfully")
    def verify_user_deleted(self):
        expect(
            self.page.locator(
                self.SUCCESS_TOAST
            )
        ).to_be_visible()

