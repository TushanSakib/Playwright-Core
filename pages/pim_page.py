import allure

from playwright.sync_api import Page
from playwright.sync_api import expect


class PIMPage:

    PAGE_HEADER = "h6"

    ADD_EMPLOYEE_MENU = "//a[text()='Add Employee']"

    FIRST_NAME = "input[name='firstName']"
    MIDDLE_NAME = "input[name='middleName']"
    LAST_NAME = "input[name='lastName']"

    SAVE_BUTTON = "button[type='submit']"

    PERSONAL_DETAILS_HEADER = (
        "//h6[text()='Personal Details']"
    )

    def __init__(self, page: Page):
        self.page = page

    @allure.step("Verify PIM page loaded")
    def verify_page_loaded(self):

        expect(
            self.page.locator(self.PAGE_HEADER)
        ).to_have_text("PIM")

    @allure.step("Open Add Employee page")
    def open_add_employee(self):

        self.page.locator(
            self.ADD_EMPLOYEE_MENU
        ).click()

    @allure.step(
        "Add employee: {first_name} {last_name}"
    )
    def add_employee(
            self,
            first_name,
            middle_name,
            last_name
    ):

        self.page.locator(
            self.FIRST_NAME
        ).fill(first_name)

        self.page.locator(
            self.MIDDLE_NAME
        ).fill(middle_name)

        self.page.locator(
            self.LAST_NAME
        ).fill(last_name)

        self.page.locator(
            self.SAVE_BUTTON
        ).click()

    @allure.step(
        "Verify employee created successfully"
    )
    def verify_employee_created(self):

        expect(
            self.page.locator(
                self.PERSONAL_DETAILS_HEADER
            )
        ).to_be_visible()