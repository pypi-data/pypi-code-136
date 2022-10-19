from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
search=input("Search")


driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("https://www.google.com")
driver.find_element(By.NAME, "q").send_keys(search + Keys.RETURN)
driver.find_element(By.XPATH, '//*[@id="rso"]/div[3]/div/div/div[1]/div/a/h3').click()
images = driver.find_element(By.CLASS_NAME, 'jss1023')  

for image in images:
    name = image.find_element(By.CLASS_NAME, 'jss1053').get_attribute("href")
    print(name)