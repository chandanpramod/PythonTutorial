import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
#=====Check boxes list

checkbox=driver.find_elements(By.XPATH,"//input[@type='checkbox']")
time.sleep(2)
print()
# for i in checkbox:
#     if i.get_attribute('value')=="option1":
#         i.click()
#         print(i.get_attribute('value'))


print(len(checkbox))
for i in checkbox:
    i.click()
    time.sleep(1)
for i in checkbox:
    i.click()
    time.sleep(1)