from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
driver=webdriver.Chrome()
driver.get("https://www.yatra.com/")
driver.maximize_window()
# Cal=driver.find_element(By.XPATH,'//input[@id="BE_flight_origin_date"]').click()
# time.sleep(4)
# date=driver.find_element(By.XPATH,'//td[@id="23/11/2024"]').click()
# time.sleep(4)
# Cal2=driver.find_element(By.XPATH,'//input[@id="BE_flight_arrival_date"]').click()
# time.sleep(4)
# date2=driver.find_element(By.XPATH,'//td[@id="01/01/2025"]').click()
# time.sleep(4)
dte=driver.find_element(By.XPATH,'//input[@id="BE_flight_origin_date"]').click()
time.sleep(4)
all_dates=driver.find_elements(By.XPATH,'//div[@id="monthWrapper"]')
time.sleep(4)
# print(len(all_dates))
for i in all_dates:
    if i.get_attribute('data-date')=="31/08/2025":
        time.sleep(4)
        i.click()
        break
    time.sleep(3)
