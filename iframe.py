from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
# to access iframe we need to have name or ID of frame
# by defauld we are at defauld content.
# now we need to switch on frame1 and access

frame1=driver.switch_to.frame("product")

# perform actions here and once done and wanted move to another frame, now we need to move
# to defauil content first and then next frame and So on

# driver.switch_to.default_content()
# frame2=driver.switch_to.frame("product")
# perform actions here and once done and wanted move to another frame, now we need to move
# to defauil content first and then next frame and So on

# driver.switch_to.default_content()
# frame3=driver.switch_to.frame("Value of ID or Name")
# perform actions here and once done and wanted move to another frame, now we need to move
# to defauil content first and then next frame and So on






time.sleep(1)
driver.close()