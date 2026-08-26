import allure

from pages.admin_page import AdminPage
from pages.components.side_menu_component import (
    SideMenuComponent
)


@allure.feature("Admin")
@allure.story("Delete User")
@allure.severity(
    allure.severity_level.CRITICAL
)
def test_delete_user(
        logged_in_page,
        created_user
):

    menu = SideMenuComponent(
        logged_in_page
    )

    menu.open_admin()

    admin_page = AdminPage(
        logged_in_page
    )

    admin_page.search_user(
        created_user["username"]
    )

    admin_page.delete_user()

    admin_page.verify_user_deleted()