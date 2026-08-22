import allure

from pages.admin_page import AdminPage
from pages.components.side_menu_component import SideMenuComponent


@allure.feature("Admin")
@allure.story("Edit User")
@allure.severity(
    allure.severity_level.CRITICAL
)
def test_edit_user(
        logged_in_page,
        created_user
):

    menu = SideMenuComponent(logged_in_page)
    menu.open_admin()

    admin_page = AdminPage(
        logged_in_page
    )
    admin_page.search_user(
        created_user["username"]
    )
    admin_page.open_user_for_edit()
    admin_page.update_user_status()
    admin_page.verify_user_updated()