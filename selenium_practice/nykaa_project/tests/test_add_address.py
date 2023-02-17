from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from time import sleep


def test_run():
    driver = webdriver.Chrome()
    driver.get("https://www.nykaa.com/")
    driver.maximize_window()
    # main_page = driver.current_window_handle
    # sleep(5)
    driver.find_element(By.XPATH, "//button[@aria-label='Kebab menu']").click()
    # sleep(5)
    # for handle in driver.window_handles:
    #     if handle != main_page:
    #         login_page = handle

    # driver.switch_to.window(login_page)
    driver.find_element(By.CSS_SELECTOR, "button:nth-child(2)").click()
    # driver.switch_to.window(driver.window_handles[1])
    # driver.find_element(By.XPATH, "//button[normalize-space()='Google']").click()
    driver.find_element(By.XPATH, "//div[@jsname='bQIQze']").click()
    driver.find_element(By.XPATH, "//input[@name='password']").send_keys("test_mail93")

    sleep(4)


# test_run()
