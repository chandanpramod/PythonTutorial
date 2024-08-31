from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
class xpath:
    def xpath_ele(self):

        # ser_obj=Service(r"C:\Users\Admin\Desktop\Testing-44\Chrome Driver\chromedriver-win64\chromedriver.exe")
        driver=webdriver.Chrome()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.maximize_window()
        loginid=driver.find_element(By.XPATH,"//input[@id='login-input']").send_keys('pamu@g.com')
        time.sleep(2)
        butt=driver.find_element(By.XPATH,"//button[@class='main-btn mt25']").click()
        time.sleep(4)
        phone=driver.find_element(By.XPATH,"//input[@id='signup-mobile-number']").send_keys(9089890987)
        time.sleep(2)
        pwd=driver.find_element(By.XPATH,"//input[@id='signup-password']").send_keys('Pramod@19876')
        time.sleep(2)
        Fname=driver.find_element(By.XPATH,"//input[@id='signup-user-first-name']").send_keys('Prmod')
        time.sleep(2)
        Lname=driver.find_element(By.XPATH,"//input[@id='signup-user-last-name']").send_keys('Chandan')
        time.sleep(2)
        con_but=driver.find_element(By.XPATH,"//button[@id='signup-form-continue-btn']").click()
        time.sleep(2)
        error_msg=driver.find_element(By.XPATH,"//p[@class='text-red fs-12 field-error']").text
        print(error_msg)
        if error_msg=="Title is required":
            print("Test Case Pass")
        else:
            print("Incorrect Error massage")


user1=xpath()
user1.xpath_ele()
