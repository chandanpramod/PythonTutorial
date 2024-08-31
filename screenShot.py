import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
driver=webdriver.Chrome()
driver.get("https://www.amazon.in/")
time.sleep(2)
driver.maximize_window()
scrl_down1=driver.execute_script("window.scrollBy(0, 500)")
scrl_down2=driver.execute_script("window.scrollBy(500, 1000)")
scrl_down3=driver.execute_script("window.scrollBy(1000, 1500)")
scrl_down4=driver.execute_script("window.scrollBy(1500, 2000)")
# scrl_down=driver.execute_script("window.scrollBy(0, 10000)")
# scrl_down=driver.execute_script("window.scrollBy(0, 10000)")
SC=driver.get_screenshot_as_file('C:\\Users\\Admin\\Desktop\\Testing-44\\Python\\First_sc1.png')
time.sleep(2)
scrl_up1=driver.execute_script("window.scrollBy(2000,-500)")
scrl_up2=driver.execute_script("window.scrollBy(1500,-500)")

scrl_up3=driver.execute_script("window.scrollBy(1000,-500)")
scrl_up4=driver.execute_script("window.scrollBy(500,-500)")

time.sleep(2)
