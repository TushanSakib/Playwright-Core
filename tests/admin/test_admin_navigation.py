from pages.components.side_menu_component import (
    SideMenuComponent
)


def test_open_admin_module(
        logged_in_page
):

    logged_in_page.goto(
        "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
    )

    menu = SideMenuComponent(
        logged_in_page
    )

    menu.open_admin()

    assert (
        "admin"
        in logged_in_page.url.lower()
    )