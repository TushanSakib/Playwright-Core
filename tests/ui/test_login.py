import allure

from pages.login_page import LoginPage
from utilities.config_reader import ConfigReader


@allure.feature("Login")
@allure.story("Valid Login")
def test_valid_login(page):

    login_page = LoginPage(page)

    base_url = ConfigReader.get(
        "environment",
        "base_url"
    )

    username = ConfigReader.get(
        "credentials",
        "username"
    )

    password = ConfigReader.get(
        "credentials",
        "password"
    )

    login_page.navigate(base_url)

    login_page.login(
        username=username,
        password=password
    )

    assert login_page.is_dashboard_displayed(), \
        "Dashboard was not displayed after login"