import pytest
from reportlab.pdfgen.pdfimages import PDFImage

from pages.components.side_menu_component import SideMenuComponent
from pages.pim_page import PIMPage
from utilities.data_generator import DataGenerator


@pytest.fixture
def created_employee(
        logged_in_page
):
    menu = SideMenuComponent(logged_in_page)

    menu.open_pim()

    pim = PIMPage(logged_in_page)

    pim.open_add_employee()

    employee = pim.add_employee()

    employee = pim.add_employee(
        first_name=DataGenerator.first_name(),
        middle_name=DataGenerator.middle_name(),
        last_name=DataGenerator.last_name()
    )

    pim.verify_employee_created()
    return employee