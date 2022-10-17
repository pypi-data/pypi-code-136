import sys
import time
import polling2
import traceback
from selenium import webdriver
# from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

from .data import Cleaner
from .common.logger import log
from .common.exceptions import CrawlerError

from typing import Union

# typing
WebElement = webdriver.remote.webelement.WebElement
WebDriver = Union[
    webdriver.Firefox,
    webdriver.Chrome,
    webdriver.Safari,
    webdriver.Edge
]


# lower casing
class Key(Keys):
    enter = Keys.RETURN
    esc = Keys.ESCAPE
    delete = Keys.DELETE
    down = Keys.ARROW_DOWN
    up = Keys.ARROW_UP
    tab = Keys.TAB


# used in arguments of WeElement selectors
ATTR_SELECTOR = {
    "id": By.ID,
    "name": By.NAME,
    "xpath": By.XPATH,
    "tag name": By.TAG_NAME,
    "link text": By.LINK_TEXT,
    "class name": By.CLASS_NAME,
    "css selector": By.CSS_SELECTOR,
    "partial link text": By.PARTIAL_LINK_TEXT,
}


# wedrivers suported by selenium
# see https://selenium-python.readthedocs.io/installation.html#drivers
webdrivers = {
    "firefox": {
        "webdriver": webdriver.Firefox,
        "options": webdriver.firefox.options.Options(),
        # "profile": firefox_profile,
        "url": "https://github.com/mozilla/geckodriver/releases",
    },
    "chrome": {
        "webdriver": webdriver.Chrome,
        "options": webdriver.chrome.options.Options(),
        "url": "https://chromedriver.chromium.org/downloads",
    },
    "safari": {
        "driver": webdriver.Safari,
        "options": webdriver.safari.options.Options(),
        "url": "https://webkit.org/blog/6900/webdriver-support-in-safari-10/",
    },
    "edge": {
        "driver": webdriver.Edge,
        "options": webdriver.edge.options.Options(),
        "url": "https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/",  # noqa E501
    },
}


class Crawler:
    """
     A selenium.webdriver adapter.

    An instance of Window calss cam perform a series of automated
    actions on webpages. Designed to handle sites with heavy use of
    javascript.

    Attributes
    ----------
    driver : selenium.webdriver
    timeout:
    """

    def __init__(self,
                 browser: str = "firefox",
                 headless: bool = False) -> None:  # noqa E501
        """
        Parameters
        ----------
        browser : str, optional
            Browser of you webdriver, by default 'firefox'
        headless : bool, optional
            If True, driver will work without the
            GUI's browser, by default False
        """
        if browser not in list(webdrivers.keys()):
            message = f"Unsuported browser '{browser}'."
            message += " List of suported ones: "
            message += ", ".join(list(webdrivers.keys())) + "."
            raise CrawlerError(message)
        self.__browser = browser
        self.__driver = None
        self.__options = None
        self.__logger = log(self.__class__.__name__)
        self.timeout = 50
        try:
            self.__options = webdrivers[browser]["options"]
            if headless:
                self.__options.headless = True
            driver = webdrivers[browser]["webdriver"]
            self.__driver = driver(options=self.__options)
        except WebDriverException as err:
            message = "You need to add the driver"
            message += f" for {browser} to your environment variables."
            message += f" You can download {browser}'s driver at: "
            message += webdrivers[browser]["url"]
            message += ". See more in"
            message += " https://selenium-python.readthedocs.io/installation.html#drivers"  # noqa E501
            self.logger.error(str(err))
            self.logger.error(message)
            sys.exit(1)

    def quitdriver(method):
        def inner(self, *args, **kwargs):
            try:
                return method(self, *args, **kwargs)
            except Exception as err:
                # which is better? 1 or 2
                # traceback.print_exc()  # 1
                # print(err)
                print("quitting driver...")
                self.quit()
                raise err  # 2
        return inner

    @property
    def driver(self,):
        return self.__driver

    @property
    def logger(self,):
        return self.__logger

    @quitdriver
    def goto(self, url: str):
        self.driver.get(url)
        return self

    @quitdriver
    def element(self, value, by="name", step=0.5, timeout=10):
        """
        element method.

        Select and element from current page.

        Parameters
        ----------
        value : str
            value of the attribute or tag defined in 'by'
        by : str, optional
            attribute, by default 'name'.
            See a list of attributes at ATTR_SELECTOR.keys()
        step : float, optional
            timeout step, by default 0.5
        timeout : int, optional
            timeout until throw error, by default 10

        Returns
        -------
        WebElement
            Element retrieved.
        """
        element = polling2.poll(
            lambda: self.driver.find_element(ATTR_SELECTOR[by], value),
            step=step,
            timeout=timeout,
        )
        return element

    @quitdriver
    def element_id(self, value, step=0.5, timeout=10):
        """
        element_id

        Retrieve element from current page by it's id value.

        Parameters
        ----------
        value : str
            id's value.

        step : float, optional
            timeout step, by default 0.5
        timeout : int, optional
            timeout until throw error, by default 10

        Returns
        -------
        WebElement
            Element retrieved.
        """
        return self.element(value, "id", step, timeout)

    @quitdriver
    def elements(self, value, by="name", step=0.5, timeout=10):
        element = polling2.poll(
            lambda: self.driver.find_elements(ATTR_SELECTOR[by], value),
            step=step,
            timeout=timeout,
        )
        return element

    @quitdriver
    def child_of(self, element, value, by="name", step=0.5, timeout=10):
        child = polling2.poll(
            lambda: element.find_element(ATTR_SELECTOR[by], value),
            step=step,
            timeout=timeout,
        )
        return child

    @quitdriver
    def children_of(self, element, value, by="name", step=0.5, timeout=10):
        children = polling2.poll(
            lambda: element.find_elements(ATTR_SELECTOR[by], value),
            step=step,
            timeout=timeout,
        )
        return children

    @quitdriver
    def click_element(self, element):
        wait = WebDriverWait(self.driver, self.timeout)
        wait.until(EC.visibility_of(element))
        wait.until(EC.element_to_be_clickable(element)).click()

    @quitdriver
    def click(self, value, by="name", step=0.5, timeout=10):
        elem = self.element(value, by=by, step=step, timeout=timeout)
        self.click_element(elem)
        return elem

    @quitdriver
    def click_id(self, id_value, step=0.5, timeout=10):
        return self.click(id_value, "id", step=step, timeout=timeout)

    @quitdriver
    def send_to_element(self, element: WebElement, key, enter=False):
        """
        send_key similar to Window.send

        Send 'key' to WebElement 'element'

        Parameters
        ----------
        element : WebElement
            Valid WebElement from selenium.
        key : Valid Selenium key or text.

        Returns
        -------
        WebElement
            Element which key was sent to.
        """
        element.send_keys(key)
        if enter:
            element.send_keys(Key.enter)

    @quitdriver
    def send(self,
             key,
             value: str,
             by="name",
             enter=False,
             step=0.5,
             timeout=10):
        """
        send

        Send a valid 'key' to element with selector 'by' and
        corresponding 'value'.

        Parameters
        ----------
        key : Valid Selenium key or text.
        value : str
            _description_
        by : str, optional
            _description_, by default 'name'
        step : float, optional
            timeout step, by default 0.5
        timeout : int, optional
            timeout until throw error, by default 10

        Returns
        -------
        WebElement
            Element which key was sent to.
        """
        elem = self.element(value, by=by, step=step, timeout=timeout)
        self.send_to_element(elem, key, enter)

    @quitdriver
    def arrow_down_element(self, element, n_times: int = 1, enter=False):
        """
        arrow_down

        Press keyboard arrow down n_times at
        element.

        Parameters
        ----------
        element : WebElement
            Valid WebElement from selenium
        n_times : int, optional
            Number of times pressing down key, by default 1
        """
        wait = WebDriverWait(self.driver, self.timeout)
        for _ in range(n_times):
            wait.until(EC.element_to_be_clickable(element)).send_keys(Key.down)
        if enter:
            wait = WebDriverWait(self.driver, self.timeout)
            wait.until(
                EC.element_to_be_clickable(element)
            ).send_keys(Key.enter)

    @quitdriver
    def arrow_down(self, value: str,
                   by="name",
                   step=0.5,
                   timeout=10,
                   n_times: int = 1,
                   enter=False):
        """
        arrow_down

        Select element by given selector 'by' and
        corresponding value, then send keyboard
        arrow down n_times.

        Parameters
        ----------
        value : str
            value of the selected attributes
        by : str, optional
            attribute, by default "name"
        step : float, optional
            timeout setp, by default 0.5
        timeout : int, optional
            timeout, by default 10
        n_times : int, optional
            times of pressing arrow up, by default 1
        enter : bool, optional
            If True, 'enter' key is sent to element, by default False
        """
        element = self.element(value, by, step, timeout)
        self.arrow_down_element(element, n_times, enter)

    @quitdriver
    def arrow_up_element(self, element, n_times: int = 1, enter=False):
        """
        arrow_down

        Presse keyboard arrow up n_times

        Parameters
        ----------
        element : WebElement
            Valid WebElement from selenium
        n_times : int, optional
            Number of times pressing down key, by default 1
        """
        wait = WebDriverWait(self.driver, self.timeout)
        for _ in range(n_times):
            wait.until(EC.element_to_be_clickable(element)).send_keys(Key.up)
        if enter:
            wait = WebDriverWait(self.driver, self.timeout)
            wait.until(
                EC.element_to_be_clickable(element)
            ).send_keys(Key.enter)

    @quitdriver
    def arrow_up(self, value: str,
                 by="name",
                 step=0.5,
                 timeout=10,
                 n_times: int = 1,
                 enter=False):
        """
        arrow_up

        Select element by given selector 'by' and
        corresponding value, then send keyboard
        arrow up n_times.

        Parameters
        ----------
        value : str
            value of the selected attributes
        by : str, optional
            attribute, by default "name"
        step : float, optional
            timeout setp, by default 0.5
        timeout : int, optional
            timeout, by default 10
        n_times : int, optional
            times of pressing arrow up, by default 1
        enter : bool, optional
            If True, 'enter' key is sent to element, by default False
        """
        element = self.element(value, by, step, timeout)
        self.arrow_up_element(element, n_times, enter)

    @quitdriver
    def get_items(self, parent, click=True):
        if click:
            self.click_element(parent)
        ul_element = self.child_of(parent, "ul", "tag name")
        li_element = self.children_of(ul_element, "li", "tag name")
        if click:
            self.click_element(parent)
        return li_element

    @quitdriver
    def scroll_page(self,):
        body = self.element("body", "tag name")
        self.send_to_element(body, Keys.PAGE_DOWN)

    @quitdriver
    def google(self, query, step=0.5, timeout=10):
        self.goto("https://google.com")
        search_bar = self.get_element("q", "name", step=step, timeout=timeout)
        search_bar.send_keys(query)
        search_bar.send_keys(Key.enter)
        # time.sleep(3)
        results = self.get_element("rso", "id")
        return results.find_elements(By.TAG_NAME, "a")

    @quitdriver
    def source(self,):
        return self.driver.page_source

    def close(self,):
        """Closes the current window."""
        self.driver.close()

    def quit(self, clean=False):
        """Quits the driver and close every associated window."""
        self.driver.quit()
        if clean:
            try:
                print("cleaning browser's data...")
                cleaner = Cleaner[self.__browser]()
                cleaner.clear_data()
                self.logger.info("Browser's data cleared.")
                print("Done!")
            except Exception as e:
                print(e, "Couldn't clean browser's data.")


def main():
    crawler = Crawler()
    crawler.goto("https://google.com")
    time.sleep(3)
    crawler.quit()


if __name__ == "__main__":
    main()
