driver.get("https://jqueryui.com/droppable/")

driver.maximize_window()

driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@class='demo-frame']")) elem1= driver.find_element(By.ID, "draggable")

elem2 = driver.find_element(By.ID, "droppable")

#ActionChains(driver).drag_and_drop(elem1, elem2).perform()

ActionChains(driver).drag_and_drop_by_offset(elem1, 100, 100).perform()

time.sleep(4)