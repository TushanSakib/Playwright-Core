# pages/login_page.py

from playwright.sync_api import Page


class LoginPage:

    USERNAME = "input[name='username']"
    PASSWORD = "input[name='password']"
    LOGIN_BUTTON = "button[type='submit']"

    def __init__(self, page: Page):
        self.page = page

    def login(self, username, password):

        self.page.fill(
            self.USERNAME,
            username
        )

        self.page.fill(
            self.PASSWORD,
            password
        )

        self.page.click(
            self.LOGIN_BUTTON
        )