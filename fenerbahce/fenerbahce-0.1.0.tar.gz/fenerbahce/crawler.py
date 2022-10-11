import requests
from bs4 import BeautifulSoup


class Crawler:
    def get_soup(self, url):
        page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        return BeautifulSoup(page.content, 'lxml')
