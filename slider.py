from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import time

#-----Move to Right-Ele1
e1=driver webdriver.Chrome (executable_path=ChromeDriverManager().install())

driver.get("https://www.snapdeal.com/products/mobiles-mobile-phones?sort=plrty") driver.maximize_window()

#elem1 = driver.find_element(By.XPATH, "//a{contains(@class, 'left-handle")]")

elem2= driver.find_element(By.XPATH, "//a[contains(@class, 'right-handle')]")

ActionChains(driver).drag_and_drop_by_offset(elem1, 60, 8).perform()

ActionChains(driver).click_and_hold(elem1).pause(1).move_by_offset(50, 0).release().perform()

ActionChains(driver).move to_element(elemi).pause(1).click_and_hold(elemi).move_by_offset(80, 0).perform()
time.sleep(4)

#-----Move to Left-Ele2
ActionChains(driver).move  to_element(elem2).pause(1).click_and_hold(elem2).move_by_offset(-80, 0).perform()
time.sleep(4)
ActionChains(driver).drag_and_drop_by_offset(elem1, 60, 8).perform()

ActionChains(driver).click_and_hold(elem2).pause(1).move_by_offset(-50, 0).release().perform()

ActionChains(driver).move  to_element(elem2).pause(1).click_and_hold(elem2).move_by_offset(-80, 0).perform()
time.sleep(4)