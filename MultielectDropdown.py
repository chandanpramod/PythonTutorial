from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
class DropDown:
    def Multiple_Dropdown(self):
        driver=webdriver.Chrome()
        driver.get("https://demo.mobiscroll.com/select/multiple-select")
        # Mul_sel=Select(driver.find_element(By.XPATH,"//select[@id='multiple-select']"))
        Mul_sel = Select(driver.find_element(By.CSS_SELECTOR, "#multiple-select"))
        time.sleep(4)
        Mul_sel.select_by_index(1)
        Mul_sel.select_by_visible_text('Clothing & Jewelry')
        Mul_sel.select_by_value("2")
        time.sleep(1)
        Mul_sel.deselect_by_index(1)
        Mul_sel.deselect_by_visible_text('Clothing & Jewelry')
        Mul_sel.deselect_by_value("2")
        time.sleep(2)
        Mul_sel.deselect_all()
        time.sleep(2)

user=DropDown()
user.Multiple_Dropdown()