import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
driver=webdriver.Chrome()
driver.get("https://www.yatra.com")
time.sleep(2)
driver.maximize_window()
# TEXT1=driver.find_element(By.CLASS_NAME,"whyBookContent")
# a=(TEXT1).text
# print(a)
# if a =="On Yatra.com, you can tailor your trip from end-to-end by scouring suitable flights and making your flight booking before proceeding with your hotel bookings. Yatra’s vast hotel repository will see you through this process seamlessly. Any intervening journey can be conveniently planned by searching up relevant train connectivity and making an IRCTC ticket booking. Look up well-researched holiday packages, sift through cruise packages and finalise your entire trip on just one platform.":
#     print('test case pass')
# else:
#     print("Fail")

Val=driver.find_element(By.XPATH,"//input[@id='BE_flight_flsearch_btn']").get_attribute('Search Flights')
print(Val)
