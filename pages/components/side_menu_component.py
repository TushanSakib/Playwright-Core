from playwright.sync_api import Page

import allure

class SideMenuComponent:

    ADMIN_MENU = "//span[text()='Admin']"
    PIM_MENU = "//span[text()='PIM']"
    LEAVE_MENU = "//span[text()='Leave']"
    RECRUITMENT_MENU = "//span[text()='Recruitment']"
    MY_INFO_MENU = "//span[text()='My Info']"

    def __init__(self,page:Page):
        self.page = page

    @allure.step("Navigate to Admin module")
    def open_admin(self) -> None:
        self.page.locator(self.ADMIN_MENU).click()

    @allure.step("Navigate to PIM module")
    def open_pin(self) -> None:
        self.page.locator(self.PIM_MENU).click()

    @allure.step("Navigate to Leave module")
    def open_leave(self)->None:
        self.page.locator(self.LEAVE_MENU).click()

    @allure.step("Navigate to Recruitment module")
    def open_recruitment(self)-> None:
        self.page.locator(self.RECRUITMENT_MENU).click()

    @allure.step("Navigate to My Info Module")
    def open_my_info(self)-> None:
        self.page.locator(self.MY_INFO_MENU).click()