import shutil
from selenium import webdriver
import os
import socket
import subprocess
import sys
import time
from datetime import datetime
# 解析配置文件
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
# 多开浏览器
from selenium_utils.colors import Logger

class MultipleChromeUtils:
    def __init__(self, chrome_path):
        self.chrome_path = chrome_path

    def open_chrome(self, num, chrome_path, chrome_port, is_cache_clear=True, is_headless=False, new_window=''):
        chrome_data_name = r'C:\selenium\chrome_data'
        chrome_data_path = chrome_path
        Logger.info(chrome_data_path)
        try:
            if os.path.exists(chrome_data_path) and is_cache_clear is True:
                Logger.info("清空缓存")
                shutil.rmtree(chrome_path)
            pass
        except:
            pass
        chrome_port_list = []
        for port_num in range(chrome_port, chrome_port + num):
            if not self.check_port('127.0.0.1', port_num):
                chrome_data = os.path.join(chrome_data_name, str(port_num))
                chrome = self.chrome_path
                if is_headless:
                    cmd = ['"'+chrome+'"', " --new-window \"www.baidu.com\"", "--headless ",
                           "--remote-debugging-port={} ".format(port_num), '--user-data-dir={} '.format(chrome_data),
                           '--new-window {} '.format(new_window)]
                else:
                    cmd = ['"'+chrome+'"', " --new-window ", new_window, "--disable-popup-blocking ",
                           "--remote-debugging-port={} ".format(port_num), '--user-data-dir={}'.format(chrome_data)]
                subprocess.Popen(''.join(cmd),shell=True)
                Logger.info(cmd)
                Logger.info('启动浏览器...')
            chrome_port_list.append(port_num)
        return chrome_port_list

    # 判断端口是否打开
    def check_port(self, ip, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((ip, int(port)))
            s.shutdown(2)
            # 利用shutdown()函数使socket双向数据传输变为单向数据传输。shutdown()需要一个单独的参数，
            # 该参数表示了如何关闭socket。具体为：0表示禁止将来读；1表示禁止将来写；2表示禁止将来读和写。
            # print('%s is open' % port)
            return True
        except Exception as e:
            return False

    # 试用限制
    def check_time(self, date_str, date_format='%Y-%m-%d'):
        if datetime.strptime(date_str, date_format) < datetime.now():
            print('超过使用期限，请联系程序开发人员。')
            time.sleep(5)
            sys.exit(999)

    def init_browser(self, chrome_port, browser_type='chrome', env='prd', timeout=5, download_path=None,
                     is_headless=False,
                     driver_path='driver\\chromedriver.exe'):
        # 构建chrome参数
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
        chrome_options = Options()
        chrome_options.add_argument('user-agent={}'.format(user_agent))
        chrome_options.add_argument('--log-level=1')
        # chrome_options.add_argument("-–user-agent=iphone 12")
        s = Service(driver_path)
        if is_headless:
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--window-size=1920,1080")
            chrome_options.add_argument("--start-maximized")
        chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:{}".format(chrome_port))
        browser = webdriver.Chrome(service=s, options=chrome_options)
        # browser.implicitly_wait(timeout)  # 隐式等待
        # self.browser.find_elements(By.XPATH ,)
        browser.implicitly_wait(10)
        return browser


if __name__ == '__main__':
    # print(check_port('127.0.0.1', 9222))
    # subprocess.getstatusoutput(["start", r"C:\Program Files\Google\Chrome\Application\chrome.exe", ])
    os.system(r'"C:\Program Files\Google\Chrome\Application\chrome.exe" --new-window --disable-popup-blocking --remote-debugging-port=90001 --user-data-dir=C:\selenium\chrome_data\90001')
    # current = os.getcwd()
    # chromePath = current + "\\chrome\\bin\\chrome.exe"
    # chrome = MultipleChromeUtils()
    # print(chrome.open_chrome(2, chromePath, 9422, is_cache_clear=False,
    #                          new_window='https://etax.hebei.chinatax.gov.cn/bszm-web/apps/views-zj/index/index.html'))
    # drvier = chrome.init_browser(9422)
    # drvier1 = chrome.init_browser(9423)
    # print(drvier.title)
    # print(drvier1.title)
