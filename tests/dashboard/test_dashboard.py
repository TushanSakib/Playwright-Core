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