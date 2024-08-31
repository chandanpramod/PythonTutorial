from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
driver=webdriver.Chrome()
driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe_frameborder_css")
driver.maximize_window()
#switch ifame by name:
# driver.switch_to.frame("iframeResult")
#switch ifame by locator:
driver.switch_to.frame(driver.find_element(By.XPATH,'//iframe[@id="iframeResult"]'))
#switch ifame by ID:
# driver.switch_to.frame("iframeResult")
driver.switch_to.frame(0)
time.sleep(2)
driver.find_element(By.XPATH,"(//a[@class='w3-right w3-btn'][1]").click()
time.sleep(4)