import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
driver=webdriver.Chrome()
driver.get("https://www.amazon.in/")
time.sleep(2)
driver.maximize_window()
scrl=driver.execute_script("window.scrollBy(900, 8000)")

time.sleep(2)