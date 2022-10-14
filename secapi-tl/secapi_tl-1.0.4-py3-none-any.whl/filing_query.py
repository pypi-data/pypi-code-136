from typing import List
from warnings import warn
from openDateRange import DateRange
from .request import Request
from .key_mapper import get_cik

# list of keys for all existing metadata points
FILING_INFORMATION_KEYS = ['accessionNumber',
                           'filingDate',
                           'reportDate',
                           'acceptanceDateTime',
                           'act',
                           'form',
                           'fileNumber',
                           'filmNumber',
                           'items',
                           'size',
                           'isXBRL',
                           'isInlineXBRL',
                           'primaryDocument',
                           'primaryDocDescription']

JSON_FILE = ".json"
BASE_URL_SUBMISSIONS = r'https://data.sec.gov/submissions/'

CIK_STRING = r'CIK'
REQUIRED_CIK_LENGTH = 10


def get_filings(ticker_symbol: str,
                date_from: str = None,
                date_to: str = None,
                form_types: List[str] = None,
                filing_information: List[str] = None) -> List[dict]:
    """
    This method returns the metadata for all filings of the given form types that belong to the company
    with the given ticker and have been filed within the given daterange.
    The returned metadata only contains the datapoints given in the filing_information parameter.
    The ticker symbol is the only information that must be given.
    If the form_type parameter is set to None all form types will be returned.
    If the filing_information parameter is set to None all metadata points will be returned.
    """

    search_daterange = DateRange(date_from=date_from, date_to=date_to)
    checker = create_filing_checker(search_daterange, form_types)
    if filing_information is None:
        information_keys = FILING_INFORMATION_KEYS
    else:
        information_keys = [i for i in FILING_INFORMATION_KEYS if i in filing_information]
        # proofs if the filing_information parameter contains metadata points that do not exist
        if len(information_keys) < len(filing_information):
            warn("filing_information list contains key that does not exist")

    # get the main submissions file
    cik = get_cik(ticker_symbol)
    length_diff = REQUIRED_CIK_LENGTH - len(cik)
    cik_formatted = ('0' * length_diff) + cik
    submissions_url = BASE_URL_SUBMISSIONS + CIK_STRING + cik_formatted + JSON_FILE

    response = Request.sec_request(url=submissions_url)
    submissions_dict = response.json()

    filings = []
    # parse recent
    data = submissions_dict['filings']['recent']
    if search_daterange.intersects(date_from=data['filingDate'][-1], date_to=data['filingDate'][0]):
        filings += filter_filings(data, checker, information_keys, cik, ticker_symbol)

    # parse files
    files = submissions_dict['filings']['files']
    for file in files:
        if search_daterange.intersects(date_from=file['filingFrom'], date_to=file['filingTo']):
            url = BASE_URL_SUBMISSIONS + file['name']
            response = Request.sec_request(url=url)
            data = response.json()
            filings += filter_filings(data, checker, information_keys, cik, ticker_symbol)

    return filings


def filter_filings(raw_filings, checker, required_information, cik, ticker_symbol):
    filings = []

    dates = raw_filings['filingDate']
    forms = raw_filings['form']
    for i, (date, form) in enumerate(zip(dates, forms)):
        if checker(date, form):
            filing = {'tickerSymbol': ticker_symbol.upper(), 'cik': cik}
            for key in required_information:
                filing[key] = raw_filings[key][i]
            filings.append(filing)
    return filings


def create_filing_checker(date_range, form_types):
    def filing_checker(filing_date, form):
        return filing_date in date_range and (form_types is None or form in form_types)
    return filing_checker
