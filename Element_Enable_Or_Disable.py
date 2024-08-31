from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
driver=webdriver.Chrome()
driver.get("https://training.openspan.com/login")
signin_but=driver.find_element(By.XPATH,"//input[@id='login_button']").is_enabled()
print(signin_but)
if signin_but=='True':
     print('Element is Enable')
else:
    print("Element is diable")

name=driver.find_element(By.XPATH,"//input[@id='user_name']").send_keys('pramod')
time.sleep(2)
pwd=driver.find_element(By.XPATH,"//input[@id='user_pass']").send_keys('passsword')
time.sleep(2)
signin_but1=driver.find_element(By.XPATH,"//input[@id='login_button']").is_enabled()
time.sleep(2)
print(signin_but1)
if signin_but1=='True':
     print('Element is Enable')
else:
    print("Element is diable")

