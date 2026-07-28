import allure

from pages.base_page import BasePage


class LoginPage(BasePage):

    USERNAME_INPUT = "input[name='username']"
    PASSWORD_INPUT = "input[name='password']"
    LOGIN_BUTTON = "button[type='submit']"

    DASHBOARD_HEADER = "//h6[text()='Dashboard']"

    def __init__(self, page):
        super().__init__(page)

    @allure.step("Enter username: {username}")
    def enter_username(self, username):
        self.fill(self.USERNAME_INPUT, username)

    @allure.step("Enter password")
    def enter_password(self, password):
        self.fill(self.PASSWORD_INPUT, password)

    @allure.step("Click Login button")
    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    @allure.step("Login with valid credentials")
    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    @allure.step("Verify Dashboard page is displayed")
    def is_dashboard_displayed(self):
        return self.is_visible(self.DASHBOARD_HEADER)