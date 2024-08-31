from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import time
driver=webdriver.Chrome()
driver.get("https://www.yatra.com/")
driver.maximize_window()
act=ActionChains(driver)
ele=driver.find_element(By.XPATH,'(//a[@class="dropdown-toggle"])[2]')
act.move_to_element(ele).perform()

time.sleep(2)
cu=driver.find_element(By.XPATH,"//a[text()='Check Your Refund']").click()
time.sleep(5)
