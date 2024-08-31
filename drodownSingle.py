from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
class DropDown:
    def Single_Dropdown(self):
        driver=webdriver.Chrome()
        driver.get("https://www.facebook.com/r.php?locale=en_GB&display=page")
        Day=Select(driver.find_element(By.XPATH,"//select[@id='day']"))
        time.sleep(4)
        Day.select_by_index(8)
        Mon=Select(driver.find_element(By.CSS_SELECTOR,'#month'))
        time.sleep(4)
        Mon.select_by_visible_text('Apr')
        Year=Select(driver.find_element(By.XPATH,'//select[@id="year"]'))
        time.sleep(4)
        Year.select_by_visible_text('1990')
        time.sleep(2)
user=DropDown()
user.Single_Dropdown()