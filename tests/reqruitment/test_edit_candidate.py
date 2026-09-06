import allure

from pages.components.side_menu_component import SideMenuComponent
from pages.recruitment_page import RecruitmentPage


@allure.feature("Recruitment")
@allure.story("Edit Candidate")
@allure.severity(allure.severity_level.CRITICAL)
def test_edit_candidate(logged_in_page,created_candidate):

    menu = SideMenuComponent(logged_in_page)

    menu.open_recruitment()

    recruitment = RecruitmentPage(logged_in_page)

    recruitment.search_candidate(
        created_candidate["candidate_name"]
    )

    recruitment.open_candidate_for_editing()
    recruitment.update_candidate_vacancy()
    recruitment.verify_candidate_updated()