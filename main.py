from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import time

# Get Website
driver = webdriver.Chrome("chromedriver.exe")
driver.get("https://www.youtube.com/user/krishnaik06")

# Accept Cookies and Click button
time.sleep(0.5)
button_accept = driver.find_element(By.XPATH, "/html/body/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/form[2]/div/div/button")
button_accept.send_keys(Keys.ENTER)

# Go to Videos
time.sleep(0.5)
button_videos = driver.find_element(By.XPATH, "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/div[3]/ytd-c4-tabbed-header-renderer/tp-yt-app-header-layout/div/tp-yt-app-header/div[2]/tp-yt-app-toolbar/div/div/tp-yt-paper-tabs/div/div/tp-yt-paper-tab[2]")
button_videos.send_keys(Keys.ENTER)

# Scroll Down the Site
time.sleep(3)
driver.execute_script("window.scrollTo(0, 5000)")
time.sleep(3)
driver.execute_script("window.scrollTo(0, 10000)")

# Get Video Title
title = driver.find_elements(By.ID, "video-title")
title_list = []
for i in range(0, 50):
    title_list.append(title[i].text)
print(title_list)
print(len(title_list))

# Get Video Link
time.sleep(3)
link = driver.find_elements(By.ID, "video-title-link")
link_list = []
for i in range(0, 50):
    link_list.append(link[i].get_attribute("href"))
print(link_list)
print(len(link_list))

# Get Thumbnail funktioniert noch nicht!
time.sleep(3)
thumbnail = driver.find_elements(By.ID, "img")
thumbnail_list = []
for i in range(0, 50):
    thumbnail_list.append(thumbnail[i].get_attribute("src"))
print(thumbnail_list)
print(len(thumbnail_list))
