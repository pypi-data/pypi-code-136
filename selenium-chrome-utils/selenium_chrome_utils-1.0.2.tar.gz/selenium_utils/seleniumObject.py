import os
import socket
import subprocess
from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium_utils.browser_utils import BrowserUtils
from selenium_utils.colors import Logger
from selenium_utils.logo import print_photo
from selenium_utils.multiple_chrome_utils import MultipleChromeUtils

'''
@auth wdx
@date 2022/10/15
@desc this a selenium utils 
@qq 540667132

'''
log = Logger()


class SeleniumUtils(BrowserUtils):
    logger = Logger()
    def __init__(self, debug=False, system=False, multiple=False):
        super().__init__()
        print_photo()
        if debug:
            self.driver = self.debug_connect_chrome()
        elif system:
            self.system_open()
        elif multiple:
            self.ports = self.multiple_chrome_open()
        else:
            log.error('customer')
        log.info('thank you for using')

    # debug模式打开
    def debug_connect_chrome(self, port=9222, executable_path='driver\\chromedriver.exe', chromePath=None):
        isOPend = self.__check_port("127.0.0.1", port)
        if not isOPend:
            self.__debugOpen(port, chromePath=chromePath)
        option = webdriver.ChromeOptions()
        option.debugger_address = "127.0.0.1:%s" % port
        service = Service(executable_path=executable_path)
        self.driver = webdriver.Chrome(options=option, service=service)
        return self.driver

    # 系统浏览器打开
    def system_open(self, executable_path='driver\\chromedriver.exe',chromePath=None):
        if chromePath is None:
            chromePath = self.chrome_path
        log.error(chromePath)
        service = Service(executable_path=executable_path)
        chrome_options = Options()
        chrome_options.binary_location = chromePath
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        return self.driver

    # 获取浏览器端口
    def multiple_chrome_open(self, nums=1, executable_path='driver\\chromedriver.exe', port=90000):
        mu = MultipleChromeUtils(self.chrome_path)
        chromePortList = mu.open_chrome(num=nums, chrome_path=executable_path, chrome_port=port)
        return chromePortList

    # debug
    def __debugOpen(self, port=92222, chromePath=None):
        if chromePath is None:
            chromePath = self.chrome_path
        print(chromePath)

        subprocess.Popen('"'+chromePath+'"'+ ' --remote-debugging-port=%s --user-data-dir="C:\selenum\AutomationProfile"' % port,shell=True)
        return port

    # 检查浏览器是否打开
    def __check_port(self, ip, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((ip, int(port)))
            s.shutdown(2)
            # 利用shutdown()函数使socket双向数据传输变为单向数据传输。shutdown()需要一个单独的参数，
            # 该参数表示了如何关闭socket。具体为：0表示禁止将来读；1表示禁止将来写；2表示禁止将来读和写。
            # print('%s is open' % port)
            log.error('浏览器已打开')
            return True
        except Exception as e:
            return False

    # 打开多个浏览器
    def open_chrome_for_multiple(self, port):
        mu = MultipleChromeUtils(self.chrome_path)
        self.driver = mu.init_browser(port)
        return self.driver

    #
    def find_by_xpath(self, x, count=3,log_print=True):
        while count > 0:
            count -= 1
            try:
                return self.driver.find_element(By.XPATH, x)
            except:
                if log_print:
                    log.error("find_by_xpath() 找不到此obj:%s" % x)
        return None

    def finds_by_xpath(self, x, count=3,log_print=True):
        while count > 0:
            count -= 1
            try:
                return self.driver.find_elements(By.XPATH, x)
            except:
                if log_print:
                    log.error("finds_by_xpath() 找不到此obj:%s" % x)
        return []

    def find_by_css(self, x, count=3,log_print=True):
        while count > 0:
            count -= 1
            try:
                return self.driver.find_element(By.CLASS_NAME, x)
            except:
                if log_print:
                    log.error("find_by_css() 找不到此obj:%s" % x)
        return None

    def finds_by_css(self, x, count=3,log_print=True):
        while count > 0:
            count -= 1
            try:
                return self.driver.find_elements(By.CLASS_NAME, x)
            except:
                if log_print:
                    log.error("finds_by_css() 找不到此obj:%s" % x)
        return []

    def find_by_id(self, x, count=3,log_print=True):
        while count > 0:
            count -= 1
            try:
                return self.driver.find_element(By.ID, x)
            except:
                if log_print:
                    log.error("find_by_id() 找不到此obj:%s" % x)
        return None

    def finds_by_id(self, x, count=3,log_print=True):
        while count > 0:
            count -= 1
            try:
                return self.driver.find_elements(By.ID, x)
            except:
                if log_print:
                    log.error("finds_by_id() 找不到此obj:%s" % x)
        return []

    def find_by_object(self, obj, x, count=3,log_print=True):
        while count > 0:
            count -= 1
            try:
                return self.driver.find_element(obj, x)
            except:
                if log_print:
                    log.error("find_by_object() 找不到此obj:%s" % x)
        return None

    def finds_by_object(self, obj, x, count=3):
        while count > 0:
            count -= 1
            try:
                return self.driver.find_elements(obj, x)
            except:
                log.error("finds_by_object() 找不到此obj:%s" % x)
        return []

    def click_element(self, obj):
        try:
            self.driver.execute_script("arguments[0].click();", obj)
            return True
        except Exception as e:
            log.error("click_element() click fail")
            return False

    def set_text(self, obj, context, isClear=True):
        try:
            if isClear:
                self.clear_input(obj)
                sleep(1)
            obj.send_keys(context)
            sleep(0.5)
        except Exception as e:
            log.error("setInputText()-->" + context + "--->" + str(e))

    def clear_input(self, o):
        o.send_keys(Keys.CONTROL, 'a')
        o.send_keys(Keys.DELETE)


if __name__ == '__main__':
    s = SeleniumUtils(system=True)
