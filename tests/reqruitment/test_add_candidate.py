import allure

from pages.components.side_menu_component import SideMenuComponent
from pages.recruitment_page import RecruitmentPage
from utilities.data_generator import DataGenerator


@allure.feature("Recruitment")
@allure.story("Add Candidate")
@allure.severity(
    allure.severity_level.CRITICAL
)
def test_add_candidate(logged_in_page):
    menu = SideMenuComponent(logged_in_page)

    menu.open_recruitment()
    recruitment_page = (
        RecruitmentPage(logged_in_page)
    )

    recruitment_page.verify_page_loaded()
    recruitment_page.create_candidate(
        first_name=DataGenerator.first_name(),
        middle_name = DataGenerator.middle_name(),
        last_name=DataGenerator.last_name(),
        email=DataGenerator.email()
    )
    recruitment_page.verify_candidate_created()