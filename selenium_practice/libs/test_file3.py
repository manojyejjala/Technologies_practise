from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_run():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    search_box = driver.find_element(By.XPATH, "//button[normalize-space()='Google']")
    search_box.send_keys("python")

    time.sleep(5)

    search_box.submit()

    driver.back()
    print(driver.tittle)

    time.sleep(3)

    driver.forward()

test_run()
