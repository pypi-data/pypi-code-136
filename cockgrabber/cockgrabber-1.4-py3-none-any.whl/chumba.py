# import argparse
import datetime
import psycopg2
import pytesseract
import time
import random
import undetected_chromedriver.v2 as uc

from twocaptcha import TwoCaptcha
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
DATABASE_URL="postgresql://victor:6OkPKgBQrktuaqnH2RgCzg@free-tier4.aws-us-west-2.cockroachlabs.cloud:26257/postal?sslmode=prefer&options=--cluster%3Dtundra-badger-3949"

written = 0
goal = random.randint(50, 60)

def wait(secs=0):
    time.sleep(secs + random.random())

def solveRecaptcha(sitekey, url):
    solver = TwoCaptcha("8a587be4fe022de5e80be77f35da99ae")
    try:
        result = solver.recaptcha(
            sitekey=sitekey,
            url=url)
    except Exception as e:
        print(e)
    else:
        return result

def login(driver, username, password):
    print("Logging in...")
    driver.get("https://login.chumbacasino.com/")

    try:
        username_box = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.NAME, "email")))
        # username_box = driver.find_element(By.XPATH, "//*[@id=\"1-email\"]")
        # wait(2)
        username_box.send_keys(username)

        # password_box = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/form/div/div/div/div[2]/div[2]/span/div/div/div/div/div/div/div/div/div[2]/div[3]/div[2]/div/div/input")
        # wait(2)
        password_box = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.NAME, "password")))
        password_box.send_keys(password)
        # wait()
        password_box.send_keys(Keys.ENTER)
        print("Logged in")
    except TimeoutException:
        print("Login boxes not found")

    try:
        daily_bonus_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "daily-bonus__claim-btn")))
        daily_bonus_button.click()
        print("Daily bonus claimed")
    except TimeoutException:
        print("Daily bonus modal not found")

def postal(driver, conn, username):
    global written

    while written < goal:
        try:
            print("Finding offer close button")
            offer_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "offer__close")))
            offer_button.click()
            print("Offer closed")
        except TimeoutException:
            print("Offer modal not found")

        try:
            print("Finding footer button")
            footer_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "footer__postal-request-code")))
            footer_button.click()
            print("Footer button clicked")
        except TimeoutException:
            print("Failed to find footer button")
            driver.save_screenshot('screenie1.png')
            raise

        try:
            print("Finding postal request button")
            postal_request_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "get-postal-request-code")))
            postal_request_button.click()
            print("Postal request button clicked")
        except TimeoutException:
            print("Failed to find postal request button")
            driver.save_screenshot('screenie5.png')
            raise

        try:
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "iframe[title='reCAPTCHA']")))
        except TimeoutException:
            print("Failed to find captcha")
            raise

        print("Solving captcha")
        # driver.save_screenshot('captcha1.png')
        res = solveRecaptcha(
            "6LfvyQ0iAAAAAGBPXO2PBIW1JLftMPb47T8IxORq",
            "https://payments.vgwgroup.net/"
        )
        print("Captcha solved")
        # driver.save_screenshot('captcha2.png')

        code = res["code"]

        # driver.save_screenshot('captcha3.png')
        driver.execute_script(
            "___grecaptcha_cfg.clients['0']['V']['V']['callback'](" "'" + code + "')"
        )

        prc_image = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[style*='border: 3px solid']")))

        prc_image.screenshot("code.png")
        prc = pytesseract.image_to_string("code.png").strip()

        # with open("chumba-codes.txt", "a") as myfile:
        #     myfile.write(prc + "\n")
        #     print("Wrote new code: ", prc)

        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO postal_codes (postal_code, casino_name, user_email, generate_time) VALUES (%s, %s, %s, now());", (prc, "chumba", username)
            )
        conn.commit()
        print("Wrote new code: ", written, prc)
        written += 1

        try:
            print("Finding return button")
            return_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "return")))
            return_button.click()
            print("Return button clicked")
        except TimeoutException:
            print("Failed to find return button")
            driver.save_screenshot('screenie6.png')
            raise

        print("Waiting, current time is ", datetime.datetime.now().time())
        wait(300)

def get_chumba(username, password):
    global written

    # parser = argparse.ArgumentParser()
    # parser.add_argument("Username")
    # parser.add_argument("Password")
    # parser.add_argument("-t", "-tesseract", action="store")
    # args = parser.parse_args()

    options = uc.ChromeOptions()
    driver = uc.Chrome(options=options)

    # if hasattr(args, "tesseract"):
    #     pytesseract.pytesseract.tesseract_cmd = args.tesseract

    conn = psycopg2.connect(DATABASE_URL)

    while written < goal:
        # login(driver, args.Username, args.Password)
        login(driver, username, password)
        try:
            postal(driver, conn, username)
        except Exception as e:
            print("Postal failed with error: ", e)
