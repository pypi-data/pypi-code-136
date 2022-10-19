import time
import random
import undetected_chromedriver.v2 as uc

from twocaptcha import TwoCaptcha
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

USERNAME = "victor10216@gmail.com"
PASSWORD = "Gmailiscool1"

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

def login(driver):
    print("Logging in...")
    driver.get("https://play.globalpoker.com/login?platform=globalpoker.com")

    try:
        username_box = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.NAME, "email")))
        # username_box = driver.find_element(By.XPATH, "//*[@id=\"1-email\"]")
        # wait(2)
        username_box.send_keys(USERNAME)

        # password_box = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/form/div/div/div/div[2]/div[2]/span/div/div/div/div/div/div/div/div/div[2]/div[3]/div[2]/div/div/input")
        # wait(2)
        password_box = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.NAME, "password")))
        password_box.send_keys(PASSWORD)
        # wait()
        password_box.send_keys(Keys.ENTER)
        print("Logged in")
    except TimeoutException:
        print("Login boxes not found")

def postal(driver):
    try:
        print("Finding get coins button")
        # get_coins_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "cashier-button")))
        get_coins_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "cashier-button")))
        get_coins_button.click()
        print("Get coins button clicked")
    except TimeoutException:
        print("Failed to find get coins button")
        driver.save_screenshot('screenie1.png')
        raise
    
    try:
        print("Finding play for free button")
        play_for_free_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Play for Free')]")))
        play_for_free_button.click()
        print("Play for free button clicked")
    except TimeoutException:
        print("Failed to find play for free button")
        driver.save_screenshot('screenie2.png')
        raise

    while True:
        try:
            print("Finding click here button")
            postal_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Click here')]")))
            postal_button.click()
            print("Click here button clicked")
        except TimeoutException:
            print("Failed to find click here button")
            driver.save_screenshot('screenie3.png')
            raise

        # wait(4)

        try:
            print("Finding IFrame")
            # iframe = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.TAG_NAME, "iframe")))
            # driver.switch_to.frame(iframe)
            WebDriverWait(driver, 5).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe[src*='https://payments.vgwgroup.net']")))
            print("Switched to IFrame")
        except TimeoutException:
            print("Failed to find IFrame")
            driver.save_screenshot('screenie4.png')
            raise

        # iframe = driver.find_elements(By.TAG_NAME,'iframe')[0]
        # driver.switch_to.frame(iframe)

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
        driver.save_screenshot('captcha1.png')
        res = solveRecaptcha(
            "6LfvyQ0iAAAAAGBPXO2PBIW1JLftMPb47T8IxORq",
            "https://payments.vgwgroup.net/"
        )
        print("Captcha solved")
        driver.save_screenshot('captcha2.png')

        code = res["code"]

        driver.save_screenshot('captcha3.png')
        # driver.execute_script(
        # "document.getElementById('g-recaptcha-response').innerHTML = " + "'" + code + "'")
        driver.execute_script(
            "___grecaptcha_cfg.clients['0']['O']['O']['callback'](" "'" + code + "')"
        )

        prc = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "p[style*='border-radius: 9px']"))).text

        with open("gp-codes.txt", "a") as myfile:
            myfile.write(prc + "\n")
            print("Wrote new code: ", prc)

        try:
            print("Finding return button")
            return_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "return")))
            return_button.click()
            print("Return button clicked")
        except TimeoutException:
            print("Failed to find return button")
            driver.save_screenshot('screenie6.png')
            raise
        
        driver.switch_to.default_content();
        wait(300)

def main():
    options = uc.ChromeOptions()
    driver = uc.Chrome(options=options)

    while True:
        login(driver)
        try:
            postal(driver)
        except Exception as e:
            print("Postal failed with error: ", e)

    

if __name__ == "__main__":
    main()