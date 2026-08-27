import allure
from playwright.sync_api import Page
from playwright.sync_api import expect

class RecruitmentPage:
    PAGE_HEADER = "h6"

    ADD_BUTTON = (
        "//button[normalize-space()='Add']"
    )

    FIRST_NAME = (
        "input[name='firstName']"
    )
    MIDDLE_NAME = (
        "input[name='middleName']"
    )
    LAST_NAME = (
        "input[name='lastName']"
    )

    EMAIL = (
        "(//input[contains(@class,'oxd-input')])[3]"
    )
    SAVE_BUTTON = (
        "//button[@type='submit']"
    )
    SUCCESS_TOAST = (
        "//p[contains(@class,'oxd-text--toast-message')]"
    )

    def __init__(self,page:Page):
        self.page = page

    @allure.step("Verify Recruitment Page Loaded")
    def verify_page_loaded(self):
        expect(
            self.page.locator(
                self.PAGE_HEADER
            )
        ).to_have_text("Recruitment")

    @allure.step("Open Add Candidate Page")
    def open_add_candidate(self):
        self.page.locator(
            self.ADD_BUTTON
        ).click()
    @allure.step("Create Candidate")
    def create_candidate(self,
                         first_name,
                         middle_name,
                         last_name,
                         email):
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
            self.EMAIL
        ).fill(email)

        self.page.locator(
            self.SAVE_BUTTON
        ).click()

    @allure.step("Verify Candidate Created")
    def verify_candidate_created(self):
        expect(
            self.page.locator(
                self.SUCCESS_TOAST
            )
        ).to_be_visible()

