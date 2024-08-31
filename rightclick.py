from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import time
driver=webdriver.Chrome()
driver.get("https://demo.guru99.com/test/simple_context_menu.html")
driver.maximize_window()
act=ActionChains(driver)
# #=========Right click--
# ele=driver.find_element(By.XPATH,'//span[text()="right click me"]')
# act.context_click(ele).perform()
# time.sleep(4)
#----------Double click----------
dc=driver.find_element(By.XPATH,'//button[text()="Double-Click Me To See Alert"]')
act.double_click(dc).perform()
time.sleep(4)