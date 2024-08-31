from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
# driver=webdriver.Chrome()
# driver.get("https://www.facebook.com/login.php")
# time.sleep(1)
# par_link=driver.find_element(By.PARTIAL_LINK_TEXT,"for").click()
# time.sleep(1)
# genderF=driver.find_element(By.XPATH,"//label[text()='Female']").click()
# time.sleep(1)
# genderMF=driver.find_element(By.XPATH,"//label[text()='Male']").click()

#==============================================================================================
driver=webdriver.Chrome()
driver.get("https://www.facebook.com/login.php")
time.sleep(3)
driver.maximize_window()
forpwd=driver.find_element(By.LINK_TEXT,"Forgotten account?").click()
time.sleep(3)
heading=driver.find_element(By.XPATH,"//h2[text()='Find Your Account']").text
if heading=='Find Your Account':
    print('Heding is correct')
else:
    print('Fail')
msg=driver.find_element(By.XPATH,"//div[text()='Please enter your email address or mobile number to search for your account.']").text
if msg=='Please enter your email address or mobile number to search for your account.':
    print('msg correct')
else:
    print('Fail')
eml=driver.find_element(By.XPATH,"//input[@id='identify_email']").send_keys('P@g.com')
search=driver.find_element(By.XPATH,"//button[@id='did_submit']").click()
time.sleep(2)
er1=driver.find_element(By.XPATH,"//div[text()='No search results']").text
if er1=='No search results':
    print('Error1 correct')
else:
    print('Incorrect er1')

er2=driver.find_element(By.XPATH,"//div[text()='Your search did not return any results. Please try again with other information.']").text
if er2=='Your search did not return any results. Please try again with other information.':
    print('Error2 correct')
else:
    print('Incorrect er2')
cancel=driver.find_element(By.XPATH,"//a[@role='button']").click()










