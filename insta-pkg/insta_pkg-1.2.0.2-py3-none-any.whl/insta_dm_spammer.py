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



class Insta_Auto_DM_Spammer(object):
    def __init__(self,login_user,login_password,target,Timeout,message,count):

        """
        count는 15이하로만 적어주세요.
        """

        if int(count) >= 15:
            input("도배 횟수는 15회 이상 넘어가면 안됩니다!")
        else:    
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



            self.client.get(f"https://www.instagram.com/direct/new")

            sleep(3)

            self.search = WebDriverWait(self.client, Timeout).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/div[2]/div/div[1]/div/div[2]/input')))
            self.search.send_keys(target)
            sleep(1)
            WebDriverWait(self.client, Timeout).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/div[2]/div/div[2]/div/div/div[3]/button'))).click()
            sleep(1)
            WebDriverWait(self.client, Timeout).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/div[1]/header/div/div[2]/button'))).click()
            sleep(1)

            for i in range(1,count+1):
                sleep(0.8)
                text_input = WebDriverWait(self.client, Timeout).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/div[2]/div/div/div[2]/div/div/div/textarea')))
                text_input.send_keys(message)
                WebDriverWait(self.client, Timeout).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/div[2]/div/div/div[2]/div/div/div[2]'))).click()
                print(f"[SUCCESS] - {message} Send!")
            input(f"전송이 완료되었습니다!\n총 갯수 : {count}\n보내신 메세지 : {message}\n보낸 사람 : {login_user}\n받는사람 : {target}\n\n프로그램이 종료 되었습니다.\n아무키나 누르면 종료 됩니다!")            

            


           




            