import allure

from pages.pim_page import PIMPage
from pages.components.side_menu_component import (
    SideMenuComponent
)
from utilities.data_generator import (
    DataGenerator
)


@allure.feature("PIM")
@allure.story("Add Employee")
@allure.severity(allure.severity_level.CRITICAL)
def test_add_employee(logged_in_page):

    menu = SideMenuComponent(
        logged_in_page
    )

    menu.open_pim()

    pim_page = PIMPage(
        logged_in_page
    )

    pim_page.open_add_employee()

    employee = pim_page.add_employee(
        first_name=DataGenerator.first_name(),
        middle_name=DataGenerator.middle_name(),
        last_name=DataGenerator.last_name()
    )

    pim_page.verify_employee_created()

    allure.attach(
        str(employee),
        name="Created Employee",
        attachment_type=
        allure.attachment_type.TEXT
    )