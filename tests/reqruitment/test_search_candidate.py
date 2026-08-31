import allure

from pages.components.side_menu_component import SideMenuComponent
from pages.recruitment_page import RecruitmentPage


@allure.feature("Recruitment")
@allure.story("Search Candidate")
@allure.severity(allure.severity_level.CRITICAL)

def test_search_candidate(
        logged_in_page,
        created_candidate
):
    menu = SideMenuComponent(logged_in_page)

    menu.open_recruitment()

    recruitment_page = (
        RecruitmentPage(logged_in_page)
    )

    recruitment_page.verify_candidate_created(created_candidate)
    recruitment_page.verify_candidate_found(created_candidate)

