from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
driver=webdriver.Chrome()
driver.get("https://www.yatra.com/")
driver.maximize_window()
cw=driver.current_window_handle
driver.find_element(By.XPATH,'//a[text()="View All"]').click()
time.sleep(2)
all_win=driver.window_handles
driver.switch_to.window(all_win[1])
VD=driver.find_element(By.XPATH,'(//span[text()="View Details"][1])').click()
time.sleep(2)
driver.switch_to.window(all_win[0])
time.sleep(4)
driver.switch_to.window(all_win[1])
time.sleep(5)
