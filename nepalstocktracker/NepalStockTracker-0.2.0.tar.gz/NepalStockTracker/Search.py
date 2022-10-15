import re
import requests
from bs4 import BeautifulSoup

try:  # When used as a package
    from NepalStockTracker import exceptions

except ImportError:  # When used as a normal script
    import exceptions


class Search:
    '''
    Gets information of the given company by the user.
    Also gets the list of companies names
    '''

    def __init__(self, ShowErrorMessage, CheckInternet, master=None):
        self.master = master
        self.CheckInternet = CheckInternet
        self.DEFAULTTEXT = 'COMPANY SYMBOL'
        self.ShowErrorMessage = ShowErrorMessage
        self.MarketURL = 'https://merolagani.com/CompanyDetail.aspx?symbol='
        self.CompanyURL = 'https://merolagani.com/handlers/AutoSuggestHandler.ashx?type=Company'

    def GetCompaniesNameList(self):
        '''Get all company names and its abbreviation from mero lagani website'''

        if self.CheckInternet():
            source = requests.get(self.CompanyURL)
            contents = source.json()

            companies = [content['l'] for content in contents]
            companies = list(filter(lambda x: not x.lower().startswith('test'), companies))
            companies.sort()

            return companies

        else:
            if self.master:
                self.master.after(250, lambda: self.ShowErrorMessage('Failed to get Company Names. No Internet.\nPress Control + R to retry.', _time=5000))

            return [self.DEFAULTTEXT]

    def get_data(self, CompanySymbol):
        '''Get given company information'''

        full_url = self.MarketURL + CompanySymbol

        if self.CheckInternet():
            page = requests.get(full_url)  # Getting information of the given company
            soup = BeautifulSoup(page.content, "html.parser")

            company_name = soup.findAll(id="ctl00_ContentPlaceHolder1_CompanyDetail1_companyName")[0].text  # Extracting company name

            if company_name:
                share_value = soup.findAll(id="ctl00_ContentPlaceHolder1_CompanyDetail1_lblMarketPrice")[0].text  # Extracting market price
                sector = soup.findAll("td", {"class": "text-primary"})[0].text.strip()  # Extracting sector of the company
                change = soup.findAll(id="ctl00_ContentPlaceHolder1_CompanyDetail1_lblChange")[0].text  # Extracting percentage change of the company

                # Extracting date of transaction done by the company
                date_pattern = re.compile(r'\d+/\d+/\d+ \d+:\d+:\d+')
                date = re.search(date_pattern, page.text)

                if date is None:  # When no date is available
                    date = ''

                else:
                    date = date.group()

                # Extracting high and low value of the company
                high_low_pattern = re.compile(r'\d+[,\d+]\d+[.\d+]\d+-\d+[,\d+]\d+[.\d+]\d+')
                high_low = re.search(high_low_pattern, page.text)

                if high_low is None:
                    high_low = '0.00-0.00'

                else:
                    high_low = high_low.group(0)

                index = page.text.index('120 Day Average')
                average_value = page.text[index: index + 200].split()[6]

                return {'company_name': company_name,
                        'sector': sector,
                        'market_price': share_value,
                        'change': change,
                        'last_traded_on': date,
                        'high_low': high_low,
                        'average': average_value
                    }

            else:
                raise exceptions.CompanyNotFoundError(f'{CompanySymbol} not found')

        else:
            raise exceptions.ConnectionError('No internet connection')

    def Profit_Loss_Or_Neutral(self, CompanySymbol):
        '''Return if the given company\'s value have been increased, decrease or nothing'''

        full_url = self.MarketURL + CompanySymbol

        page = requests.get(full_url)  # Getting information of the given company
        soup = BeautifulSoup(page.content, "html.parser")
        changed = soup.findAll(id="ctl00_ContentPlaceHolder1_CompanyDetail1_lblMarketPrice")[0].prettify()

        return changed
