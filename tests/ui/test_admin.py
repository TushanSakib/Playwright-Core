# tests/admin/test_admin_navigation.py

from pages.admin_page import AdminPage
from pages.components.side_menu_component import SideMenuComponent


def test_open_admin_module(logged_in_page):

    side_menu = SideMenuComponent(
        logged_in_page
    )

    side_menu.open_admin()

    admin_page = AdminPage(
        logged_in_page
    )

    admin_page.verify_page_loaded()