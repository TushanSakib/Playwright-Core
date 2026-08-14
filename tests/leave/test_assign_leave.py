import allure

from pages.components.side_menu_component import SideMenuComponent
from pages.leave_page import LeavePage


@allure.feature("Leave")
@allure.story("Assign Leave")
@allure.severity(allure.severity_level.CRITICAL)

def test_assign_leave(logged_in_page):
    menu = SideMenuComponent(logged_in_page)

    menu.open_leave()

    leave_page = LeavePage(logged_in_page)

    leave_page.verify_page_loaded()

    leave_page.open_assign_leave()

    leave_page.assign_leave(
        employee_name="Linda Anderson",
        from_date="2026-20-08",
        to_date="2026-22-08",
        comment="Automation test leave"
    )
    leave_page.verify_leave_assigned()