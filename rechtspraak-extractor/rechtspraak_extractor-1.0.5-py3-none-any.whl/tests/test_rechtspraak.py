from test_rechtspraak_api import get_rechtspraak
from test_rechtspraak_metadata_api_pp import get_rechtspraak_metadata

get_rechtspraak(max_ecli=100, sd='2022-08-01')
get_rechtspraak_metadata()