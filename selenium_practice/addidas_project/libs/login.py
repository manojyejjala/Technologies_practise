from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait, Select
from time import sleep


def run():
    driver = webdriver.Chrome()
    driver.get("https://www.adidas.co.in/")
    driver.maximize_window()
    # main_page = driver.current_window_handle
    # sleep(5)
    driver.find_element(
        By.XPATH, "//a[@manual_cm_sp='header-_-customerinfo-_-log in ']").click()
    sleep(5)
    # for handle in driver.window_handles:
    #     if handle != main_page:
    #         login_page = handle

    # driver.switch_to.window(login_page)

    driver.find_element(
        By.ID, "login-email").send_keys("test.mail199302@gmail.com")
    sleep(5)
    driver.find_element(By.XPATH, "//span[normalize-space()='SHOW']").click()
    sleep(5)
    driver.find_element(By.ID, "login-password").send_keys("Test_mail93")
    sleep(10)
    driver.find_element(By.CLASS_NAME, "gl-checkbox__input").click()
    sleep(10)
    driver.find_element(
        By.CSS_SELECTOR, "button[aria-label='Log in'] span[role='img']").click()
    sleep(10)
    driver.find_element(By.ID, "ACCOUNT").click()
    sleep(5)
    driver.find_element(
        By.XPATH, "//span[normalize-space()='Log me out']").click()
    sleep(5)
    driver.find_element(
        By.XPATH, "//span[normalize-space()='Yes, Log me out']").click()
    sleep(5)
