from boatrace.official.v1707.pages.monthly_schedule_page.location import (
    create_monthly_schedule_page_url,
)


def test_create_monthly_schedule_page_url():
    assert (
        create_monthly_schedule_page_url(2022, 9)
        == "https://boatrace.jp/owpc/pc/race/monthlyschedule?year=2022&month=9"
    )
