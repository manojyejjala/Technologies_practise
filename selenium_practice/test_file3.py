rom selenium import webdriver
import time

driver = webdriver.chrome()
driver.get("https://www.google.com")

search_box = driver.find_element_by_name("q")
search_box.send_keys("python")

time.sleep(5)

search_box.submit()

driver.back()
print(driver.tittle)

time.sleep(3)

driver.forward()