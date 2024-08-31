import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
# inp=driver.find_element(By.CSS_SELECTOR,"#name").send_keys('Pramod')
# alt_but=driver.find_element(By.XPATH,"//input[@id='alertbtn']").click()
# time.sleep(2)
# popup1=driver.switch_to.alert
# print(popup1.text)
# popup1.accept()
# time.sleep(1)
# popup1.dismiss()

# con_but=driver.find_element(By.XPATH,"//input[@id='confirmbtn']").click()
# time.sleep(1)
# popup2=driver.switch_to.alert
# print(popup2.text)
# popup2.accept()
# popup2.dismiss()
# time.sleep(1)
# driver.close()


