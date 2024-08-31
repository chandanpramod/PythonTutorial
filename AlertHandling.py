import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
driver=webdriver.Chrome()
driver.get("https://demoqa.com/alerts")
time.sleep(2)
prompt=driver.find_element(By.CSS_SELECTOR,"#promtButton").click()
time.sleep(1)
popup=driver.switch_to.alert
popup.send_keys("Hi I Am pramod")