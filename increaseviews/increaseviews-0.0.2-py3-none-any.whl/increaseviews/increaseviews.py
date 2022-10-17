from selenium import webdriver
import random
import time

def use_chrome(path,link,repetition,sleeptime_1,sleeptime_2):
    driver = webdriver.Chrome(path)
    for i in range(int(repetition)):
        print("No of times repeated is " + str(i))
        driver.get(link)
        sleep_time = random.randint(sleeptime_1,sleeptime_2)
        time.sleep(sleep_time)
    driver.quit()

def chr_morethanone(path,number_of_videos,link_list,repetition,sleeptime_1,sleeptime_2):
    driver = webdriver.Chrome(path)
    videos = link_list
    for i in range(int(repetition)):
        print("No of times runned " + str(i))
        random_video = random.randint(0,number_of_videos-1)
        driver.get(videos[random_video])
        sleep_time = random.randint(sleeptime_1,sleeptime_2)
        time.sleep(sleep_time)
    driver.quit()

def use_edge(path,link,repetition,sleeptime_1,sleeptime_2):
    driver = webdriver.Edge(path)
    for i in range(int(repetition)):
        print("No of times repeated is " + str(i))
        driver.get(link)
        sleep_time = random.randint(sleeptime_1,sleeptime_2)
        time.sleep(sleep_time)
    driver.quit()

def edge_morethanone(path,number_of_videos,link_list,repetition,sleeptime_1,sleeptime_2):
    driver = webdriver.Edge(path)
    videos = link_list
    for i in range(int(repetition)):
        print("No of times runned " + str(i))
        random_video = random.randint(0,number_of_videos-1)
        driver.get(videos[random_video])
        sleep_time = random.randint(sleeptime_1,sleeptime_2)
        time.sleep(sleep_time)
    driver.quit()

#use_edge("D:\system\edgedriver_win64\msedgedriver", "https://www.youtube.com/watch?v=e68-3Iyq7aY",2,5,10)
#edge_morethanone("D:\system\edgedriver_win64\msedgedriver", 2, ['https://www.youtube.com/watch?v=8iqL7yVU2Y4','https://www.youtube.com/watch?v=pHh8ef2bdEI'], 3, 5, 10)