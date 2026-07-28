import allure

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


@allure.feature("Accessibility Scan")
def test_dashboard_accessibility(page):

    page.goto(
        "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    )

    login = LoginPage(page)

    login.login(
        "Admin",
        "admin123"
    )

    page.wait_for_timeout(5000)

    dashboard = DashboardPage(page)

    dashboard.verify_dashboard_loaded()

    print("Dashboard loaded successfully")