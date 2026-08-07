import allure

from pages.components.side_menu_component import SideMenuComponent
from pages.pim_page import PIMPage
from utilities.data_generator import DataGenerator


@allure.feature("PIM")
@allure.story("Search Employee")
def test_search_employee(logged_in_page,created_employee):

    menu = SideMenuComponent(logged_in_page)
    menu.open_pim()
    pim_page = PIMPage(logged_in_page)
    pim_page.open_employee_list()
    pim_page.search_employee(
        first_name=created_employee.first_name
    )
    pim_page.verify_employee_exists(
        first_name=created_employee.first_name
    )