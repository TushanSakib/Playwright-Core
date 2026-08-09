import allure

from pages.components.side_menu_component import SideMenuComponent
from pages.pim_page import PIMPage
from utilities.data_generator import DataGenerator


@allure.feature("PIM")
@allure.story("Edit Employeee")
@allure.severity(
    allure.severity_level.CRITICAL
)
def test_edit_employee(logged_in_page,created_employee):
    menu = SideMenuComponent(
        logged_in_page
    )

    menu.open_pim()

    pim_page = PIMPage(logged_in_page)

    pim_page.open_employee_for_edit()

    pim_page.update_nickname(
        DataGenerator.nickname()
    )

    pim_page.verify_employee_update()