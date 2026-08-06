import allure

from pages.components.side_menu_component import SideMenuComponent
from pages.pim_page import PIMPage
from utilities.data_generator import DataGenerator


@allure.feature("PIM")
@allure.story("Search Employee")
def test_search_employee(logged_in_page):

    menu = SideMenuComponent(
        logged_in_page
    )
    menu.open_pim()
    pim_page = PIMPage(
        logged_in_page
    )

    first_name = DataGenerator.first_name()
    last_name = DataGenerator.last_name()
    middle_name = DataGenerator.middle_name()
    pim_page.open_add_employee()
    employee = pim_page.add_employee(
        first_name = first_name,
        middle_name=middle_name,
        last_name=last_name
    )

    pim_page.verify_employee_created()
    menu.open_pim()
    pim_page.open_employee_list()
    pim_page.search_employee(
        first_name
    )
    pim_page.verify_employee_exists(
        first_name
    )