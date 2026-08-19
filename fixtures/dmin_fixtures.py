import pytest

from pages.admin_page import AdminPage
from pages.components.side_menu_component import SideMenuComponent
from utilities.data_generator import DataGenerator


@pytest.fixture
def created_user(logged_in_page):
    menu = SideMenuComponent(logged_in_page)

    menu.open_admin()

    admin_page = AdminPage(logged_in_page)

    admin_page.open_add_user()

    username = DataGenerator.username()

    admin_page.create_user(
        employee_name="Linda Anderson",
        username=username,
        password="Password@123"
    )
    admin_page.verify_user_created()

    return {
        "username":username
    }