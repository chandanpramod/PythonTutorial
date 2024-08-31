from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
class Democheckbox:
    def checkbox(self):
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com/flights")
        driver.maximize_window()
        B1=driver.find_element(By.XPATH,"//a[@title='Non Stop Flights']").click()
        time.sleep(4)
        sel1=driver.find_element(By.XPATH, "//a[@title='Non Stop Flights']").is_selected()
        print(sel1)
        B11 = driver.find_element(By.XPATH, "//a[@title='Non Stop Flights']").click()
        time.sleep(4)
        B3 = driver.find_element(By.XPATH, "//a[@title='Student Fare Offer']").click()
        time.sleep(4)
        sel2 = driver.find_element(By.XPATH, "//a[@title='Student Fare Offer']").is_selected()
        print(sel2)
        B31 = driver.find_element(By.XPATH, "//a[@title='Student Fare Offer']").click()
        time.sleep(4)
        B2 = driver.find_element(By.XPATH, "//a[@title='Armed Forces Offer']").click()
        time.sleep(4)
        sel3 = driver.find_element(By.XPATH, "//a[@title='Armed Forces Offer']").is_selected()
        print(sel3)
        B21 = driver.find_element(By.XPATH, "//a[@title='Armed Forces Offer']").click()
        time.sleep(4)
        B4 = driver.find_element(By.XPATH, "//a[@title='Senior Citizen Offer']").click()
        time.sleep(4)
        sel4 = driver.find_element(By.XPATH, "//a[@title='Senior Citizen Offer']").is_selected()
        print(sel4)
        B41 = driver.find_element(By.XPATH, "//a[@title='Senior Citizen Offer']").click()

        time.sleep(4)



user1=Democheckbox()
user1.checkbox()

