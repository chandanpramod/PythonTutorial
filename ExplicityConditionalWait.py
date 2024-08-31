from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver=webdriver.Chrome()
driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')
driver.implicitly_wait(5)
seach=driver.find_element(By.CSS_SELECTOR,'.search-keyword').send_keys('ber')
time.sleep(1)
driver.maximize_window()
add_crt=driver.find_elements(By.XPATH,'//button[text()="ADD TO CART"]')
# print(len(add_crt))
if len(add_crt)==3:
    print('pass')
else:
    print('fail')

for i in add_crt:
    if i.text=="ADD TO CART":
        i.click()
# time.sleep(1)
crt=driver.find_element(By.XPATH,"//img[@alt='Cart']").click()
proceed=driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
# time.sleep(2)
promo=driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
Apply=driver.find_element(By.XPATH,"//button[@class='promoBtn']").click()
success=driver.find_element(By.XPATH,"//span[text()='Code applied ..!']").text
wait=WebDriverWait(driver,15)
wait.until(EC.presence_of_element_located((By.XPATH,"//span[text()='Code applied ..!']")))

# time.sleep(10)
# success=driver.find_element(By.XPATH,"//span[text()='Code applied ..!']").text
if success=="Code applied ..!":
    print("Pass")
else:
    print("fail")






time.sleep(1)
driver.close()