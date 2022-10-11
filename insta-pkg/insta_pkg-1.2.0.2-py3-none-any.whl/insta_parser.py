from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager as CM
from time import sleep
import selenium
import requests
from bs4 import BeautifulSoup
class insta_parser(object):
    def __init__(self,login_user,login_password,target,Timeout):
        self.options = webdriver.ChromeOptions()
        #self.options.add_argument("--headless")
        self.headers = {"userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/90.0.1025.166 Mobile Safari/535.19"}
        self.options.add_experimental_option("mobileEmulation", self.headers)
        self.client = webdriver.Chrome(executable_path=CM().install(), options=self.options)
        self.client.set_window_size(1000, 1000)

        self.client.get("https://www.instagram.com/accounts/login/")

        sleep(3)

        print(f"Login as {login_user}")

        self.user = WebDriverWait(self.client, Timeout).until(EC.presence_of_element_located(( By.XPATH, '//*[@id="loginForm"]/div[1]/div[3]/div/label/input')))
        self.user.send_keys(login_user)

        
        self.passwords =  WebDriverWait(self.client, Timeout).until(EC.presence_of_element_located(( By.XPATH, '//*[@id="loginForm"]/div[1]/div[4]/div/label/input')))
        self.passwords.send_keys(login_password)

        self.lgbtn = WebDriverWait(self.client, Timeout).until(EC.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div[1]/div[6]/button')))
        sleep(0.4)
        self.lgbtn.click()

        sleep(0.3)

        sleep(2)
        print("Login finish - WhiteHole")

        sleep(0.4)


        try:
            self.r = self.client.get(f"https://www.instagram.com/{target}")
            
            self.b = BeautifulSoup(self.r.content , 'html.parser')

            self.follow = self.b.find('span',"_ac2a")
            self.name = self.b.find('span',"_aacl _aacp _aacw _aacx _aad7 _aade")
            self.followerss = self.b.find('span',"_ac2a")

            print(f"""
            아이디 : {target} 님의 정보

            이름 : {self.__annotations__name.string}
            
            """)
            self.qu = input("Discord Webhook? >> ")

            if self.qu == "y":
                pass
        except Exception as e:
            print("없는 유저거나 알 수 없는 오류가 발생하였습니다.")     




        print()

        sleep(1.5)

        


        