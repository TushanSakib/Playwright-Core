import allure

from pages.admin_page import AdminPage
from pages.components.side_menu_component import (
    SideMenuComponent
)


@allure.feature("Admin")
@allure.story("Navigation")
def test_open_admin_page(logged_in_page):

    menu = SideMenuComponent(
        logged_in_page
    )

    menu.open_admin()

    admin_page = AdminPage(
        logged_in_page
    )

    admin_page.verify_page_loaded()