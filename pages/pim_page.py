import allure

from playwright.sync_api import Page
from playwright.sync_api import expect


class PIMPage:

    ADD_EMPLOYEE_MENU = "a:has-text('Add Employee')"

    FIRST_NAME_INPUT = "input[name='firstName']"
    MIDDLE_NAME_INPUT = "input[name='middleName']"
    LAST_NAME_INPUT = "input[name='lastName']"

    SAVE_BUTTON = "button[type='submit']"

    PERSONAL_DETAILS_HEADER = (
        "//h6[text()='Personal Details']"
    )

    EMPLOYEE_ID = (
        "(//input[contains(@class,'oxd-input')])[5]"
    )
    EMPLOYEE_LIST_MENU = "a:has-text('Employee List')"
    EMPLOYEE_NAME_SEARCH = (
        "(//input[@placeholder='Type for hints...'])[1]"
    )
    SEARCH_BUTTON = (
        "//button[@type='submit']"
    )
    RESULT_TABLE = ".oxd-table-body"
    NO_RECORDS_FOUND = "text=No Records Found"

    EDIT_BUTTON = (
        "(//i[contains(@class,'bi-pencil-fill')])[1]"
    )

    NICKNAME_INPUT = (
        "(//input[contains(@class,'oxd-input')])[6]"
    )

    SAVE_PERSONAL_DETAILS_BUTTON = (
        "(//button[@type='submit'])[1]"
    )

    SUCCESS_TOAST = (
        "//p[text()='Successfully Updated']"
    )

    DELETE_BUTTON = (
        "(//i[contains(@class,'bi-trash')])[1]"
    )

    CONFIRM_DELETE_BUTTON = (
        "//button[normalize-space()='Yes, Delete']"
    )






    def __init__(self, page: Page):
        self.page = page

    @allure.step("Navigate to Add Employee page")
    def open_add_employee(self) -> None:

        self.page.locator(
            self.ADD_EMPLOYEE_MENU
        ).click()

        expect(
            self.page.locator(
                self.FIRST_NAME_INPUT
            )
        ).to_be_visible()

    @allure.step(
        "Create employee: {first_name} {middle_name} {last_name}"
    )
    def add_employee(
            self,
            first_name: str,
            middle_name: str,
            last_name: str
    ) -> dict:

        self.page.locator(
            self.FIRST_NAME_INPUT
        ).fill(first_name)

        self.page.locator(
            self.MIDDLE_NAME_INPUT
        ).fill(middle_name)

        self.page.locator(
            self.LAST_NAME_INPUT
        ).fill(last_name)

        employee_id = self.page.locator(
            self.EMPLOYEE_ID
        ).input_value()

        self.page.locator(
            self.SAVE_BUTTON
        ).click()

        return {
            "first_name": first_name,
            "middle_name": middle_name,
            "last_name": last_name,
            "employee_id": employee_id
        }

    @allure.step(
        "Verify employee creation successful"
    )
    def verify_employee_created(self) -> None:

        expect(
            self.page.locator(
                self.PERSONAL_DETAILS_HEADER
            )
        ).to_be_visible(timeout=10000)


    @allure.step("Navigate to Employee List")
    def open_employee_list(self):
        self.page.locator(
            self.EMPLOYEE_LIST_MENU
        ).click()


    @allure.step("Search employee: {employee}")
    def search_employee(self,employee_name):
        self.page.locator(
            self.EMPLOYEE_NAME_SEARCH
        ).fill(employee_name)

        self.page.locator(
            self.SEARCH_BUTTON
        ).click()

    @allure.step("Verify employee exists in search result")
    def verify_employee_exists(self,employee_name:str):
        expect(
            self.page.locator(
                self.RESULT_TABLE
            )
        ).to_contain_text(employee_name)


    @allure.step("Open employee for editing")
    def open_employee_for_edit(self):
        self.page.locator(
            self.EDIT_BUTTON
        ).click()


    @allure.step("Update employee nickname: {nickname}")
    def update_nickname(self,nickname:str):
        self.page.locator(
            self.NICKNAME_INPUT
        ).fill(nickname)

        self.page.locator(
            self.SAVE_PERSONAL_DETAILS_BUTTON
        ).click()

    @allure.step("Verify employee nickname updated successfully")
    def verify_employee_update(self):
        expect(
            self.page.locator(
                self.SUCCESS_TOAST
            )
        ).to_be_visible()


    @allure.step("Delete Employee")
    def delete_employee(self):
        self.page.locator(
            self.DELETE_BUTTON
        ).click()

        self.page.locator(
            self.CONFIRM_DELETE_BUTTON
        ).click()


    @allure.step("Verify Employee Deleted Successfully")
    def verify_employee_deleted(self):
        expect(
            self.page.locator(
                self.SUCCESS_TOAST
            )
        ).to_be_visible()
