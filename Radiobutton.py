import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
radio_but=driver.find_elements(By.XPATH,"//input[@name='radioButton']")
# print(len(radio_but))
# for i in radio_but:
#     if i.get_attribute('value')=='radio1':
#         i.click()
#         time.sleep(1)

for i in radio_but:
    i.click()
    time.sleep(1)