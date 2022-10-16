import os
import re
import webbrowser
import winreg
import zipfile
from getpass import getuser
from os import listdir
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium_utils.colors import Logger
from os.path import join as pjoin, isdir
from tqdm import tqdm

'''
@auth wdx
@date 2022/10/15
@desc 获取谷歌浏览器的驱动和环境谷歌浏览器的路径

'''

SYSTEM_PATH = pjoin(os.getenv('systemDrive'), os.sep)
CHROME_PATH = pjoin(SYSTEM_PATH, 'Users', getuser(), 'AppData', 'Local', 'Google', 'Chrome')
log = Logger()

class BrowserUtils:
    # 浏览器注册表信息
    _browser_regs = {
        'IE': r"SOFTWARE\Clients\StartMenuInternet\IEXPLORE.EXE\DefaultIcon",
        'chrome': r"SOFTWARE\Clients\StartMenuInternet\Google Chrome\DefaultIcon",
        'edge': r"SOFTWARE\Clients\StartMenuInternet\Microsoft Edge\DefaultIcon",
        'firefox': r"SOFTWARE\Clients\StartMenuInternet\FIREFOX.EXE\DefaultIcon",
        '360': r"SOFTWARE\Clients\StartMenuInternet\360Chrome\DefaultIcon",
    }

    def __init__(self):
        self.chrome_path = self.__get_browser_path('chrome')
        root_path = os.getcwd()
        if self.chrome_path is None:
            log.warning('notice: not found your chrome path,please add your chrome to system environment')
            self.chrome_path = "chrome.exe"
        driver_path = root_path + "\\driver"  # 这里需要提前手动创建号download目录
        if not os.path.exists(driver_path):
            self.__check_chrome_driver()
        if not os.path.exists(driver_path + "\\chromedriver.exe"):
            self.__check_chrome_driver()

    def __get_browser_path(self, browser):
        """
        获取浏览器的安装路径

        :param browser: 浏览器名称
        """
        try:
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, self._browser_regs[browser])
        except FileNotFoundError:
            return None
        value, _type = winreg.QueryValueEx(key, "")
        return value.split(',')[0]

    def __open_url(self, url, browsers=('IE',)):
        """
        使用指定的浏览器打开url对应的网页地址

        :param url: 网页地址
        :param browsers: 浏览器名称列表
        :return: 是否打开成功
        """
        for browser in browsers:
            path = self.get_browser_path(browser)
            if path:
                print(f'open with browser: `{browser}`, path: `{path}`')
                webbrowser.register(browser, None, webbrowser.BackgroundBrowser(path))
                webbrowser.get(browser).open(url)
                return True
        return False

    def __get_chrome_version(self):
        paths = [pjoin(SYSTEM_PATH, 'Program Files', 'Google', 'Chrome', 'Application'), pjoin(
            CHROME_PATH, 'Program Files (x86)', 'Google', 'Chrome', 'Application'), pjoin(CHROME_PATH, 'Application')]
        for i in range(len(paths)):
            try:
                dir = paths[i]
                files = listdir(dir)
                break
            except:
                pass
        for file in files:
            if isdir(pjoin(dir, file)) and file.__contains__('.'):
                return file
        return None

    def __get_version(self, file_path):
        '''查询系统内的Chromedriver版本'''
        outstd2 = os.popen(file_path + 'chromedriver --version').read()
        return outstd2.split(' ')[1]

    def __unzip_file(self, src_file, dest_dir, *password):
        if password:
            password = password.encode()
        zf = zipfile.ZipFile(src_file)
        try:
            zf.extractall(path=dest_dir, pwd=password)
        except RuntimeError as e:
            log.error(e)
        zf.close()

    def __check_chrome_driver(self, repeat_count=0):
        repeat_count += 1
        if repeat_count > 3:
            log.error(
                'sorry can not download chromedriver,\nplease go to the https://registry.npmmirror.com/-/binary/chromedriver download! thank you')
            return
        # 获取项目根路径
        root_path = os.getcwd()
        download_path = root_path + "\\driver"  # 这里需要提前手动创建号download目录
        if not os.path.exists(download_path):
            os.makedirs(download_path)
        try:
            log.info('检查浏览器驱动是否存在')
            service = Service(executable_path="driver\\chromedriver.exe")
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            chrome_options.binary_location = self.chrome_path
            webdriver.Chrome(service=service, options=chrome_options)
            log.info('恭喜您！驱动已经匹配上当前浏览器')
            self.__remove_chrome_zip()
            return
        except Exception as msg:
            log.error(msg)
            reg = "Current browser version is.+with"
            versions = self.__get_server_chrome_versions()
            chrome_version = re.search(reg, str(msg))
            if chrome_version is not None:
                chrome_version = chrome_version.group().replace("Current browser version is ", "").replace(" with", "")
            else:
                chrome_version = self.__get_chrome_version()
                if chrome_version is None:
                    chrome_version = self.__get_latest_version(versions)
            main_version = chrome_version.split('.')[0:-1]
            main_version = '.'.join(main_version)
            targetVersion = self.__find_main_server(main_version, versions)
            log.info("Chrome Version:" + chrome_version)
            url = 'https://registry.npmmirror.com/-/binary/chromedriver/%schromedriver_win32.zip' % targetVersion
            log.info(url)
            log.randlog('正在下载谷歌浏览器驱动')
            file_name = 'chromedriver_' + chrome_version.replace('/', '') + '.zip'
            self.__download(url, file_name)
            # 解压zip文件
            self.__unzip_file(file_name, download_path)
            log.info('解压完毕')
            self.__check_chrome_driver(repeat_count)

    def __find_main_server(self, version, all_version):
        for v in all_version:
            temp = v.split('.')[0:-1]
            temp = '.'.join(temp)
            if temp == version:
                return v
        return None

    def __get_server_chrome_versions(self):
        '''return all versions list'''
        versionList = []
        url = "https://registry.npmmirror.com/-/binary/chromedriver/"
        header = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}

        rep = requests.get(url, headers=header).json()
        for item in rep:
            versionList.append(item["name"])
        return versionList

    def __get_latest_version(self, versions):
        max_version = 0
        latest_version = ''
        for v in versions:
            main_version = v.split(".")[0]
            try:
                main_version = int(main_version)
                if main_version > max_version:
                    max_version = main_version
                    latest_version = v
            except:
                pass
        return latest_version

    def __remove_chrome_zip(self):
        current_path = os.getcwd()
        list_file = os.listdir()
        for file in list_file:
            chrome_zip = re.findall("chromedriver_.*", file)
            if ''.join(chrome_zip).endswith("zip"):
                try:
                    os.remove(current_path + "\\" + file)
                except:
                    pass

    def __download(self, url: str, fname: str):
        resp = requests.get(url, stream=True)
        total = int(resp.headers.get('content-length', 0))
        with open(fname, 'wb') as file, tqdm(
                desc=fname,
                total=total,
                unit='iB',
                unit_scale=True,
                unit_divisor=1024,
        ) as bar:
            for data in resp.iter_content(chunk_size=1024):
                size = file.write(data)
                bar.update(size)
