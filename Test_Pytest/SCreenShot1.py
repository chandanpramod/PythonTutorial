from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
driver=webdriver.Chrome()
driver.get("https://www.yatra.com/")
driver.maximize_window()
# scele=driver.find_element(By.XPATH,'(//input[@id="BE_flight_flsearch_btn"])[1]')
# sc1=driver.get_screenshot_as_file('C:\\Users\\Admin\\Desktop\\ScreenShots.sc1')
driver.get_screenshot_as_file("C:\\Users\\Admin\\Desktop\\ScreenShots\\sc.png")
time.sleep(2)
driver.save_screenshot("C:\\Users\\Admin\\Desktop\\ScreenShots1\\sc1.png")

