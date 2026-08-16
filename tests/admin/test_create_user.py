import allure

from pages.admin_page import AdminPage
from pages.components.side_menu_component import SideMenuComponent
from utilities.data_generator import DataGenerator


@allure.feature("Admin")
@allure.story("Create User")
def test_create_user(logged_in_page):

    side_menu = SideMenuComponent(
        logged_in_page
    )

    side_menu.open_admin()

    admin_page = AdminPage(
        logged_in_page
    )

    admin_page.verify_page_loaded()

    admin_page.open_add_user()
    admin_page.create_user(
        employee_name="Linda Anderson",
        username=DataGenerator.username(),
        password = "Password@123"
    )

    admin_page.verify_user_created()