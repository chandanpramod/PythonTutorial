from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
class RadioButtons:
    def rodiobut(self):
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com/flights")
        driver.maximize_window()
        B1=driver.find_element(By.XPATH,'//i[@class="icon icon-angle-right arrowpassengerBox"]').click()
        time.sleep(4)
        r1=driver.find_element(By.XPATH, '(//span[@class="ddlabel"])[1]').is_selected()
        print(r1)
        r11= driver.find_element(By.XPATH, '(//span[@class="ddlabel"])[2]').is_selected()
        print(r11)
        r2 = driver.find_element(By.XPATH, '(//span[@class="ddlabel"])[2]').click()
        time.sleep(4)
        r2 = driver.find_element(By.XPATH, '(//span[@class="ddlabel"])[2]').is_selected()
        print(r2)
        r1111 = driver.find_element(By.XPATH, '(//span[@class="ddlabel"])[1]').is_selected()
        print(r1111)
        r1111 = driver.find_element(By.XPATH, '(//span[@class="ddlabel"])[1]').click()
        r3 = driver.find_element(By.XPATH, '(//span[@class="ddlabel"])[3]').click()
        time.sleep(4)
        r2 = driver.find_element(By.XPATH, '(//span[@class="ddlabel"])[3]').is_selected()
        print(r3)






user1=RadioButtons()
user1.rodiobut()

