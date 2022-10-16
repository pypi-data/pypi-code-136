import urllib.parse

from boatrace.official.v1707 import BASE_URL


def create_monthly_schedule_page_url(year: int, month: int):
    return f"{BASE_URL}/owpc/pc/race/monthlyschedule?{urllib.parse.urlencode({'year': year, 'month': month})}"
