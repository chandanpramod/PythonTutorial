from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
time.sleep(2)
driver.maximize_window()
inp=driver.find_element(By.XPATH,"//input[@id='autosuggest']").send_keys('Po')
time.sleep(5)
List=driver.find_elements(By.XPATH,'//a[@class="ui-corner-all"]')
for i in List:
    if i.text=="Poland":
        i.click()
        time.sleep(1)
a= driver.find_element(By.XPATH,"//input[@id='autosuggest']").get_attribute('value')
print(a)
if a=='Poland':
    print('Test case pass')
else:
    print('test case fail')
