from utilities.network_monitor import NetworkMonitor
from utilities.soft_assertions import SoftAssert

def test_dashboard(logged_in_page):
    SoftAssert.verify_equal(
        "Dashboard",
        "Dashboard",
        "Dashboard title mismatch"
    )

    SoftAssert.verify_true(
        logged_in_page.locator(
            ".oxd-userdropdown-name"
        ).is_visible(),
        "User dropdown name not visible"
    )

def test_dashboard_network(logged_in_page):

    network = NetworkMonitor(logged_in_page)

    network.start_monitoring()
    logged_in_page.reload()
    network.attach_results()
    network.verify_no_failed_requests()