from re import T
from urllib import request
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



class Following_Parser(object):
    def __init__(self,login_user,login_password,target,count,Timeout):

        """
        count 는 원하는 상대 팔로우 수를 보고 맞춰주세요
        """
        
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--headless")
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



        self.client.get(f"https://www.instagram.com/{target}")

        sleep(1.5)

        WebDriverWait(self.client, Timeout).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/section/ul/li[2]/a'))).click()


        self.lst = []
        for i in range(1,count+1):
            self.follower = WebDriverWait(self.client, Timeout).until( EC.presence_of_element_located((By.XPATH, f'/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div[1]/div/div[{i}]/div[2]/div[1]')))
            self.real_follower = self.follower.text

            print(f"[SUCCESS] - {self.real_follower}")
            sleep(0.5)

            self.client.execute_script("arguments[0].scrollIntoView();", self.follower)

            sleep(1)

            self.lst.append(self.real_follower)

        print("Follower Load Finish!")
        #self.webhook = input("Discord Webhook? (Y/N) >> ")
        
        self.result = ' '.join(self.lst)+"\n"
       # if self.webhook == "Y" or "y":
          #  self.dis_web = input("Discord Webhook URL >> ")
          #  dt = {
               #     "username": "WhiteHole Instagram Follower Scraper",
             #       "avatar_url": "",
               #     "content": f"팔로워 목록 입니다!\n\n```\n{self.result}\n```"     
              #      }
           # requests.post(self.dis_web,json=dt)
          #  print("전송성공!")
        #elif self.webhook == "N" or "n":
        return self.result  




            