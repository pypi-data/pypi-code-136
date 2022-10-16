import os
import re

from selenium_utils.seleniumObject import SeleniumUtils

class Test(SeleniumUtils):
    def __init__(self):
        super().__init__(debug=True)

if __name__ == '__main__':
    Test()