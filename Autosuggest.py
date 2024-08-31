# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# import time
#
# driver = webdriver.Chrome()
# driver.get('https://www.yatra.com/')
# driver.maximize_window()
# depart = driver.find_element(By.XPATH, '//input[@id="BE_flight_origin_city"]').click()
# city_Search = driver.find_element(By.XPATH, '//input[@id="BE_flight_origin_city"]').send_keys('Pune')
# time.sleep(4)
# city_names = driver.find_elements(By.XPATH, '//p[@class="ac_cityname"]')
# time.sleep(4)
# print(len(city_names))
# for i in city_names:
#     if i.text == "Pune (PNQ)":
#         i.click()
# driver.close()