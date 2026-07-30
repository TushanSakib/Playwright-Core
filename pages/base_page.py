import allure
from playwright.sync_api import Page


class BasePage:

    def __init__(self, page: Page):
        self.page = page

    def click(self, locator: str):

        self.page.locator(locator).click()

    def fill(self, locator: str, value: str):

        self.page.locator(locator).fill(value)

    def get_text(self, locator: str):

        return self.page.locator(
            locator
        ).text_content()

    def is_visible(self, locator: str):

        return self.page.locator(
            locator
        ).is_visible()

    def navigate(self, url: str):

        self.page.goto(url)

    def take_screenshot(self,name:str):
        screenshot = self.page.screenshot(
            full_page=True
        )
        allure.attach(
            screenshot,
            name=name,
            attachment_type=allure.attachment_type.PNG
        )