from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
class Autosuggst_AutoconpleteDropdown:
    def autossuggcompDropdwn(self):
        driver=webdriver.Chrome()
        driver.get('https://www.yatra.com/')
        driver.maximize_window()
        depart=driver.find_element(By.XPATH,'//input[@id="BE_flight_origin_city"]').click()
        time.sleep(4)
        city_Search=driver.find_element(By.XPATH,'//input[@id="BE_flight_origin_city"]').send_keys('Pun')
        time.sleep(4)
        city_names=driver.find_elements(By.XPATH,'//p[@class="ac_cityname"]')
        time.sleep(4)
        print(len(city_names))

        for i in city_names:
            print(i.text)
            if i.text == "Pune (PNQ)":
                i.click()
                time.sleep(4)
        time.sleep(4)
        driver.find_element(By.XPATH,'//input[@id="BE_flight_arrival_city"]').send_keys('New')
        time.sleep(4)
        list_city=driver.find_elements(By.XPATH,'//div[@class="viewport"]')
        time.sleep(4)
        print(len(list_city))
        time.sleep(4)
        # for i in Dest:


p1=Autosuggst_AutoconpleteDropdown()
p1.autossuggcompDropdwn()