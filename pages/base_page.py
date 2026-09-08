import time

import allure
from playwright.sync_api import Page, expect


class BasePage:
    DEFAULT_TIMEOUT = 10000

    def __init__(self, page: Page):
        self.page = page

    def click(self, locator: str):

        self.page.locator(locator).click()

    def safe_click(self,locator:str):
        element = self.page.locator(locator)
        expect(element).to_e_visible()
        expect(element).to_be_enabled()
        element.click()

    ## Retry click method to handle transient issues
    def retry_click(self,locator:str,retries:int=2):
        for attempt in range(retries):
            try:
                self.safe_click(locator)
                return
            except Exception:
                if attempt == retries-1:
                    raise
                time.sleep(1)


    def fill(self, locator: str, value: str):

        self.page.locator(locator).fill(value)

    def safe_fill(self,locator:str,value:str):
        element = self.page.locator(locator)
        expect(element).to_be_visible()
        expect(element).to_be_enabled()
        element.clear()
        element.fill(value)

    def get_text(self, locator: str):

        return self.page.locator(
            locator
        ).text_content()

    def verify_text(self,
                    locator:str,
                    expected_text:str):
        expect(
            self.page.locator(locator)
        ).to_have_text(expected_text)


    def is_visible(self, locator: str):

        return self.page.locator(
            locator
        ).is_visible()

    def wait_for_visible(self,locator:str,):
        expect(self.page.locator(locator)).to_be_visible()

    def wait_for_hidden(self,locator:str):
        expect(self.page.locator(locator)).to_be_visible()

    def select_dropdown_option(self,
                               dropdown_locator:str,
                               option_text:str):
        self.safe_click(dropdown_locator)

        self.page.get_by_text(
            option_text,
            exact=True
        ).click()

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