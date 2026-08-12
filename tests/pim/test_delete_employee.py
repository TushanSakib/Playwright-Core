import allure

from pages.components.side_menu_component import SideMenuComponent
from pages.pim_page import PIMPage


@allure.feature("PIM")
@allure.story("Delete Employee")
@allure.severity(allure.severity_level.CRITICAL)

def test_delete_employee(
        logged_in_page,
        created_employee
):

    menu = SideMenuComponent(logged_in_page)
    menu.open_pim()

    pim_page = PIMPage(logged_in_page)

    pim_page.open_employee_list()

    pim_page.search_employee(
        created_employee["first_name"])

    pim_page.delete_employee()

    pim_page.verify_employee_deleted(created_employee["first_name"])