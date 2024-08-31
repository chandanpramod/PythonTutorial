from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
# driver=webdriver.Chrome()
# driver.get("https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp")
# ele1=driver.find_element(By.XPATH,"//div[@id='myDIV']").is_displayed()
# print(ele1)
# but=driver.find_element(By.XPATH,"//button[@onclick='myFunction()']").click()
# time.sleep(2)
# ele1=driver.find_element(By.XPATH,"//div[@id='myDIV']").is_displayed()
# print(ele1)


class stateofElement:
    def hiddenele(self):
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com/hotels")
        driver.maximize_window()
        icon=driver.find_element(By.XPATH,"//span[@class='txt-ellipses hotel_passengerBox travellerPaxBox']").click()
        time.sleep(2)
        plus=driver.find_element(By.XPATH,"(//span[@class='ddSpinnerPlus'])[2]").click()
        time.sleep(2)
        child=driver.find_element(By.XPATH,'(//span[@class="pax-title"])[3]').is_displayed()
        print(child)
        time.sleep(2)
        icon1= driver.find_element(By.XPATH, "(//span[@class='ddSpinnerMinus'])[2]").click()
        time.sleep(2)
        child = driver.find_element(By.XPATH, '(//span[@class="pax-title"])[3]').is_displayed()
        print(child)


user1=stateofElement()
user1.hiddenele()

