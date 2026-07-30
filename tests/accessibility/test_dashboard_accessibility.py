from pages.dashboard_page import DashboardPage
from utilities.accessibility_scanner import AccessibilityScanner


def test_dashboard_accessibility(
        logged_in_page
):

    dashboard = DashboardPage(
        logged_in_page
    )

    logged_in_page.goto(
        "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
    )

    dashboard.verify_page_loaded()

    scanner = AccessibilityScanner(
        logged_in_page
    )

    scanner.scan()