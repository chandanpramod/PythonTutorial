from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
class Partical_and_Link_text:
    def link_text(self):

        driver=webdriver.Chrome()
        driver.get("https://www.facebook.com/login.php")
        time.sleep(3)
        driver.maximize_window()
        forpwd=driver.find_element(By.LINK_TEXT,"Forgotten account?").click()
        time.sleep(3)
        eml=driver.find_element(By.XPATH,"//input[@id='identify_email']").send_keys('P@g.com')
        search=driver.find_element(By.XPATH,"//button[@id='did_submit']").click()
        time.sleep(5)
        cancel=driver.find_element(By.XPATH,"//a[@role='button']").click()
        time.sleep(3)
        driver.close()
    def parcial_Link_text(self):
        driver1=webdriver.Chrome()
        driver1.get("https://www.facebook.com/login.php")
        time.sleep(2)
        driver1.maximize_window()
        par_link=driver1.find_element(By.PARTIAL_LINK_TEXT,"Sign up for").click()
        time.sleep(1)
        fname=driver1.find_element(By.XPATH,"//input[@name='firstname']").send_keys('Laxman')
        time.sleep(2)
        lname=driver1.find_element(By.XPATH,"//input[@name='lastname']").send_keys('Chand')
        time.sleep(2)
        mob=driver1.find_element(By.XPATH,"//input[@name='reg_email__']").send_keys(9090909090)
        time.sleep(2)
        newpwd=driver1.find_element(By.XPATH,"//input[@name='reg_passwd__']").send_keys('Pramod@12345678')
        time.sleep(2)
        Gender=driver1.find_element(By.XPATH,"(//label[@class='_58mt'])[2]").click()
        time.sleep(3)
user1=Partical_and_Link_text()
# user1.link_text()
user1.parcial_Link_text()