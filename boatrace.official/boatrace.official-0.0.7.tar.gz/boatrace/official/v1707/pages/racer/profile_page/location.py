import urllib.parse

from boatrace.official.v1707 import BASE_URL


def create_racer_profile_page_url(racer_registration_number: int):
    return f"{BASE_URL}/owpc/pc/data/racersearch/profile?{urllib.parse.urlencode({'toban': racer_registration_number})}"
