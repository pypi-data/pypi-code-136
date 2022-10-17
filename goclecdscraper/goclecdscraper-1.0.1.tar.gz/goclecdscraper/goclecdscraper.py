import requests
from bs4 import BeautifulSoup
import os

SEARCH_URL = 'https://www.goclecd.fr/catalogue/search-'


class SearchResult:
    def __init__(self):

        self.title = None
        self.price = 0.0
        self.symbol = None
        self.href = None

    def __str__(self):
        str = ''

        str += f'Title : {self.title}'
        str += os.linesep

        str += f'price : {self.price} {self.symbol}'
        str += os.linesep

        str += f'href : {self.href}'
        str += os.linesep

        return str


class Offer:
    def __init__(self):
        self.price = 0.0
        self.currency = None
        self.coupon = None
        self.price_without_coupon = 0.0

        self.merchant = Merchant()
        self.edition = Edition()

    def __str__(self):
        str = ''

        str += f'Price : {self.price} {self.currency}'
        str += os.linesep

        str += f'Price without coupon : {self.price_without_coupon} {self.currency}'
        str += os.linesep

        str += f'Coupon : {self.coupon}'
        str += os.linesep

        str += f'Edition : {self.edition}'
        str += os.linesep

        return str


class Merchant:
    def __init__(self):
        self.id = 0
        self.name = None
        self.types = None

        self.aggregate_rating = AggregateRating()


class AggregateRating:
    def __init(self):
        self.value = 0.0
        self.count = 0


class Edition:
    def __init__(self):
        self.id = 0
        self.name = None


def currency_to_symbol(currency):
    symbol = None

    if currency == 'eur':
        symbol = '€'

    return symbol


class GoclecdScraper():
    def __init__(self):
        pass

    def get_offers(self, url, currency='eur'):
        content = requests.get(url).content

        page = BeautifulSoup(content, 'lxml')

        offers_table = page.find('div', {'class': 'offers-table x-offers'})

        product_id = page.find('a', {'class': 'aks-follow-btn aks-follow-btn-score aks-follow-btn-score-green game-aside-button jc-center col-4'})['data-product-id']

        result = requests.get(f'https://www.goclecd.fr/wp-admin/admin-ajax.php?action=get_offers&product={product_id}&currency={currency}&region=&edition=&moreq=&use_beta_offers_display=1').json()

        offers = []

        for offer_json in result['offers']:
            print(offer_json)

            offer = Offer()

            merchant_json = result['merchants'][offer_json['merchant']]
            edition_json = result['editions'][offer_json['edition']]

            offer.merchant.id = merchant_json['id']
            offer.merchant.name = merchant_json['name']

            offer.merchant.aggregate_rating.value = merchant_json['aggregateRating']['value']
            offer.merchant.aggregate_rating.count = merchant_json['aggregateRating']['count']

            offer.merchant.aggregate_rating.types = merchant_json['types']

            offer.edition.id = edition_json['id']
            offer.edition.name = edition_json['name']

            offer.currency = currency_to_symbol(currency)
            offer.price = float(offer_json['price'][currency]['price'])
            offer.price_without_coupon = float(offer_json['price'][currency]['priceWithoutCoupon'])

            offers.append(offer)

        return offers

    def search(self, search):
        content = requests.get(SEARCH_URL + search.replace(' ', '+')).content

        page = BeautifulSoup(content, 'lxml')

        result_tags = page.find_all('li', {'class' : 'search-results-row'})

        search_results = []

        for result_tag in result_tags:
            search_result = SearchResult()

            search_result.title = result_tag.find('h2', {'class': 'search-results-row-game-title'}).text
            tmp_price = result_tag.find('div', {'class': 'search-results-row-price'}).text.strip().replace(',', '.')

            search_result.price = float(tmp_price[0:-1])
            search_result.symbol = tmp_price[-1]

            search_result.href = result_tag.find('a', {'class': 'search-results-row-link'})['href']

            search_results.append(search_result)

        return search_results


if __name__ == '__main__':
    scraper = GoclecdScraper()
    search_results = scraper.search('mafia 3')

    for search_result in search_results:
        print(search_result)