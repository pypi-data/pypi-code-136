from bs4 import BeautifulSoup
import os
from fake_useragent import UserAgent
import re
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AmazonScraper:
    def __init__(self, driver=None):
        self.driver = driver

    def get_page(self, url):
        page = None

        if self.driver is None:
            ua = UserAgent()
            headers = {'User-Agent': ua.random}
            page = requests.get(url, headers=headers).content
        else:
            self.driver.get(url)
            WebDriverWait(self.driver, 30000).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#titleSection"))
            )

            page = self.driver.page_source

        return page

    def __get_product_page__(self, product_url):
        page = BeautifulSoup(self.get_page(product_url), "lxml")

        return page

    def get_product(self, product_url):

        page = self.__get_product_page__(product_url)

        product = Product()
        product.url = product_url

        product_title_tag = page.find(id="titleSection")

        if product_title_tag is None:
            return None

        tmp_evaluation = page.find('span', {'id': 'acrPopover'}).text

        product.evaluation = float(re.findall("\d+[\.|,]\d+", tmp_evaluation)[0].replace(',', '.'))

        saving_percentage_tag = page.find('span', {'class' : 'savingsPercentage'})

        if saving_percentage_tag is not None:
            product.saving_percentage = int(re.findall(r'\d+', saving_percentage_tag.text)[0])

        price_block = page.find('span', {'class' : 'priceToPay'})

        product.title = product_title_tag.text.strip()

        tmp_price = price_block.find("span", {"class": "a-price-whole"}).text
        tmp_price += price_block.find("span", {"class": "a-price-fraction"}).text

        tmp_price = tmp_price.replace(',', '.')
        product.price = float(tmp_price)

        product.price_symbol = price_block.find("span", {"class": "a-price-symbol"}).text

        return product


class Product:
    def __init__(self):
        self.title = None
        self.code = None
        self.url = None
        self.price = 0.0
        self.price_symbol = None
        self.evaluation = 0.0
        self.evaluations_count = 0
        self.saving_percentage = 0.0

    def __str__(self):
        to_string = ""
        to_string += "Title : "
        to_string += self.title
        to_string += os.linesep
        to_string += "Price : "
        to_string += str(self.price) + " " + self.price_symbol
        to_string += os.linesep
        to_string += "Evaluation : "
        to_string += str(self.evaluation)
        to_string += os.linesep
        to_string += "Evaluation count : "
        to_string += str(self.evaluations_count)
        to_string += os.linesep
        to_string += "Saving percentage : "
        to_string += str(self.saving_percentage)
        to_string += os.linesep

        return to_string
