from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get("https://www.amazon.in/mobile-phones/b/?ie=UTF8&node=1389401031&ref_=nav_cs_mobiles")
driver.maximize_window()
poco=driver.find_element(By.XPATH,"(//span[text()='POCO'])[2]").click()
time.sleep(3)
logo=driver.find_element(By.XPATH,"(//body/div[1]/header/div/div/div/div/ a)[1]").click()
time.sleep(2)