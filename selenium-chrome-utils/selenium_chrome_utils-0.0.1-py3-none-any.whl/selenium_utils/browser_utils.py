import os
import re
import webbrowser
import winreg
import zipfile
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium_utils.colors import Logger
log = Logger()
from tqdm import tqdm
'''
@auth wdx
@date 2022/10/15
@desc 获取谷歌浏览器的驱动和环境谷歌浏览器的路径

'''


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
        self.chrome_path = self.get_browser_path('chrome')
        root_path = os.getcwd()
        if self.chrome_path is None:
            log.warning('notice: not found your chrome path,please add your chrome to system environment')
            self.chrome_path="chrome.exe"
        driver_path = root_path + "\\driver"  # 这里需要提前手动创建号download目录
        if not os.path.exists(driver_path):
            self.check_chrome_driver()
        if not os.path.exists(driver_path + "\\chromedriver.exe"):
            self.check_chrome_driver()

    def get_browser_path(self, browser):
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

    def open_url(self, url, browsers=('IE',)):
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

    def get_Chrome_version(self):
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Google\Chrome\BLBeacon')
        version, types = winreg.QueryValueEx(key, 'version')
        return version

    def get_version(self, file_path):
        '''查询系统内的Chromedriver版本'''
        outstd2 = os.popen(file_path + 'chromedriver --version').read()
        return outstd2.split(' ')[1]

    def unzip_file(self, src_file, dest_dir, *password):
        if password:
            password = password.encode()
        zf = zipfile.ZipFile(src_file)
        try:
            zf.extractall(path=dest_dir, pwd=password)
        except RuntimeError as e:
            log.error(e)
        zf.close()

    def check_chrome_driver(self, repeat_count=0):
        repeat_count += 1
        if repeat_count > 3:
            log.error(
                'sorry can not download chromedriver,\nplease go to the https://registry.npmmirror.com/-/binary/chromedriver download! thank you')
            return
        # 获取项目根路径
        root_path = os.path.abspath(os.path.dirname(__file__)).replace("test", "")
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
            driver = webdriver.Chrome(service=service, options=chrome_options)
            log.info('恭喜您！驱动已经匹配上当前浏览器')
            self.__remove_chrome_zip()
            return
        except Exception as msg:
            log.error(msg)
            reg = "Current browser version is.+with"
            chrome_version = re.search(reg, str(msg))
            if chrome_version is not None:
                chrome_version = chrome_version.group().replace("Current browser version is ", "").replace(" with", "")
            else:
                versions = self.__get_server_chrome_versions()
                chrome_version = self.__get_latest_version(versions)
            versions = self.__get_server_chrome_versions()
            main_version = chrome_version.split('.')[0:-1]
            main_version = '.'.join(main_version)
            targetVersion = self.__find_main_server(main_version, versions)
            log.info("Chrome Version:" + chrome_version)
            url = 'https://registry.npmmirror.com/-/binary/chromedriver/%schromedriver_win32.zip' % targetVersion
            log.info(url)
            header = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}
            log.randlog('正在下载谷歌浏览器驱动')
            # response = requests.get(url=url, headers=header)

            file_name = 'chromedriver_' + chrome_version.replace('/', '') + '.zip'
            self.download(url, file_name)
            # 保存ChromeDriver到当前项目路径下的/download目录下
            # open(file_name, 'wb').write(response.content)
            # 解压zip文件
            self.unzip_file(file_name, download_path)
            log.info('解压完毕')
            self.check_chrome_driver(repeat_count)

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
        list_file=os.listdir()
        for file in list_file:
            chrome_zip = re.findall("chromedriver_.*", file)
            if ''.join(chrome_zip).endswith("zip"):
                try:
                    os.remove(current_path+"\\"+file)
                except:
                    pass

    def download(self,url: str, fname: str):
        # 用流stream的方式获取url的数据
        resp = requests.get(url, stream=True)
        # 拿到文件的长度，并把total初始化为0
        total = int(resp.headers.get('content-length', 0))
        # 打开当前目录的fname文件(名字你来传入)
        # 初始化tqdm，传入总数，文件名等数据，接着就是写入，更新等操作了
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

    def test(self):
        vserion = self.__get_server_chrome_versions()
        m = self.__get_latest_version(vserion)
        print(m)


if __name__ == '__main__':
        # if ''.join(chrome_zip).endswith("zip"):
        #     try:
        #         os.remove(current_path + "\\" + file)
        #     except:
        #         pass
    b = BrowserUtils()
    # path=b.get_browser_path('chrome')
    # print(path)
    b.check_chrome_driver()
