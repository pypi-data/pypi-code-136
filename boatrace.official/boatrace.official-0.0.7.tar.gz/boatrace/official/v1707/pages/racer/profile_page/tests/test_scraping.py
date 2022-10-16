import os
from datetime import date

import pytest
from boatrace.models import Branch, Prefecture, RacerRank
from boatrace.official.exceptions import DataNotFound
from boatrace.official.v1707.pages.racer.profile_page.scraping import (
    Racer,
    extract_racer_profile,
)

base_path = os.path.dirname(os.path.abspath(__file__))


def test_extract_racer_profile():
    file_path = os.path.normpath(os.path.join(base_path, "./fixtures/4444.html"))

    with open(file_path, mode="r") as file:
        data = extract_racer_profile(file)

    assert data == Racer(
        last_name="桐生",
        first_name="順平",
        registration_number=4444,
        birth_date=date(1986, 10, 7),
        height=160,
        weight=53,
        branch_prefecture=Branch.SAITAMA,
        born_prefecture=Prefecture.FUKUSHIMA,
        term=100,
        current_rating=RacerRank.A1,
    )


def test_scrape_a_no_contents_page():
    file_path = os.path.normpath(
        os.path.join(os.path.join(base_path, "./fixtures/data_not_found.html"))
    )

    with open(file_path, mode="r") as file:
        with pytest.raises(DataNotFound):
            extract_racer_profile(file)
