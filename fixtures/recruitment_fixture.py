import pytest

from pages.recruitment_page import (
    RecruitmentPage
)

from pages.components.side_menu_component import (
    SideMenuComponent
)

from utilities.data_generator import (
    DataGenerator
)


@pytest.fixture
def created_candidate(
    logged_in_page
):

    menu = SideMenuComponent(
        logged_in_page
    )

    menu.open_recruitment()

    recruitment = RecruitmentPage(
        logged_in_page
    )

    recruitment.open_add_candidate()

    first_name = (
        DataGenerator.first_name()
    )

    last_name = (
        DataGenerator.last_name()
    )

    recruitment.create_candidate(
        first_name=first_name,
        middle_name="QA",
        last_name=last_name,
        email=DataGenerator.email()
    )

    recruitment.verify_candidate_created()

    return {
        "candidate_name":
            f"{first_name} {last_name}"
    }