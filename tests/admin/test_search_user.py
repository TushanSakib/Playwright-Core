import allure

from pages.admin_page import AdminPage
from pages.components.side_menu_component import SideMenuComponent


@allure.feature("Admin")
@allure.story("Search User")
@allure.severity(allure.severity_level.CRITICAL)
def test_search_user(logged_in_page,created_user):
    menu = SideMenuComponent(logged_in_page)

    menu.open_admin()

    admin_page = AdminPage(logged_in_page)

    admin_page.search_user(created_user["username"])
    admin_page.verify_user_found(created_user["username"])