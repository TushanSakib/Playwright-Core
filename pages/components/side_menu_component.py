import allure


class SideMenuComponent:

    ADMIN_MENU = "//span[text()='Admin']"
    PIM_MENU = "//span[text()='PIM']"
    LEAVE_MENU = "//span[text()='Leave']"

    def __init__(self, page):

        self.page = page

    @allure.step(
        "Open Admin Module"
    )
    def open_admin(self):

        self.page.locator(
            self.ADMIN_MENU
        ).click()

    @allure.step(
        "Open PIM Module"
    )
    def open_pim(self):

        self.page.locator(
            self.PIM_MENU
        ).click()

    @allure.step(
        "Open Leave Module"
    )
    def open_leave(self):

        self.page.locator(
            self.LEAVE_MENU
        ).click()