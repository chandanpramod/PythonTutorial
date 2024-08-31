from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
class FndEle_byID:
      def byid(self):
          Ser_Obj=Service(r'C:\Users\Admin\Desktop\Testing-44\Chrome Driver\chromedriver-win64\chromedriver.exe')
          driver=webdriver.Chrome(service=Ser_Obj)
          driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
          driver.maximize_window()
          Login=driver.find_element(By.ID,"login-input").send_keys('pamu.chandan@gmail.com')
          Cont=driver.find_element(By.ID,'login-continue-btn').click()
          Mob=driver.find_element(By.ID,'signup-mobile-number').send_keys(9876543210)
          pwd=driver.find_element(By.ID,'signup-password').send_keys('Pramod@123456')
          Fname=driver.find_element(By.ID,'signup-user-first-name').send_keys('Pramod')
          Lname=driver.find_element(By.ID,'signup-user-last-name').send_keys('Chandan')
          # not1=driver.find_element(By.CLASS_NAME,'notif-label').click()
          # not2=driver.find_element(By.CLASS_NAME,'notif-label').click()
          but=driver.find_element(By.ID,'signup-form-continue-btn').click()


          time.sleep(5)
user1=FndEle_byID()
user1.byid()