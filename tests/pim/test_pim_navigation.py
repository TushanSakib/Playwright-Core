import allure

from pages.pim_page import PIMPage
from pages.components.side_menu_component import (SideMenuComponent)


@allure.feature("PIM")
@allure.story("Navigation")
def test_open_pim_page(logged_in_page):
    menu = SideMenuComponent(

        logged_in_page
    )

    menu.open_pim()

    pim_page = PIMPage(logged_in_page)

    pim_page.verify_page_loaded()