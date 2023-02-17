from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep


def run():

    driver = webdriver.Chrome()
    driver.get("https://www.adidas.co.in/")
    driver.maximize_window()
    sleep(5)
    driver.find_element(
        By.XPATH, "//a[@manual_cm_sp='header-_-customerinfo-_-log in ']").click()
    sleep(5)
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
        By.XPATH, "//a[normalize-space()='Address Book']").click()
    sleep(3)
    driver.find_element(
        By.XPATH, "//div[@data-auto-id='add-new-address']").click()
    sleep(4)

    # driver.find_element(By.XPATH, "//a[@role='menu'][normalize-space()='MEN']").click()
    # sleep(5)
    # driver.find_element(
    #     By.CSS_SELECTOR, "button[title='HOODIES & SWEATSHIRTS'] span").click()
    # sleep(10)
    # driver.find_element(
    #     By.XPATH, "//div[@data-auto-id='product_container']//div//div//div//div//div//div//div//div[@data-auto-id='glass-product-card']//a//div//p[@data-auto-id='product-card-title'][normalize-space()='IN SMU FZ HD']").click()
    # sleep(10)
    # driver.find_element(By.XPATH, "//span[normalize-space()='2XL']").click()
    # sleep(10)
    # driver.find_element(By.XPATH, "//button[@title='Add To Bag']").click()
    # sleep(10)
    # driver.find_element(
    #     By.XPATH, "//span[normalize-space()='View Bag']").click()
    # sleep(10)
    # driver.find_element(By.XPATH, "//button[@aria-label='Checkout']").click()
    sleep(10)
    driver.find_element(
        By.XPATH, "//input[@aria-label='First Name']").send_keys("Test")
    driver.find_element(
        By.XPATH, "//input[@aria-label='Last Name']").send_keys("mail")
    driver.find_element(
        By.XPATH, "//input[@aria-label='Street Address']").send_keys("omr road, asv chandilya")
    driver.find_element(
        By.XPATH, "//input[@aria-label='Landmark']").send_keys("OMR")
    driver.find_element(
        By.XPATH, "//input[@aria-label='Additional info']").send_keys("8th Floor")
    driver.find_element(
        By.XPATH, "//input[@aria-label='City']").send_keys("Chennai")
    driver.find_element(
        By.XPATH, "//input[@aria-label='Pin Code']").send_keys("600098")
    # state = Select(driver.find_element(By.XPATH, "//button[@title='State']")).click()
    # state.select_by_value("Tamil Nadu")
    driver.find_element(By.XPATH, "//button[@title='State']").click()
    sleep(4)
    driver.find_element(
        By.XPATH, "//button[normalize-space()='Tamil Nadu']").click()
    driver.find_element(
        By.XPATH, "//input[@aria-label='Mobile Number']").send_keys("8247472875")
    driver.find_element(
        By.XPATH, "//button[@data-auto-id='save-address']").click()
    sleep(10)
    # driver.find_element(By.XPATH, "//input[@name='saveShippingAddressOnSubmit']").click()
    # driver.find_element(By.XPATH, "//input[@id='doc-account-tnc']").click()
    # driver.find_element(By.XPATH, "//button[@aria-label='Review & Pay']").click()
    # driver.find_element(By.ID, "//button[normalize-space()='Tamil Nadu']").click()
    # driver.file_detector(By.XPATH, "//a[normalize-space()='log in']").click()
    # sleep(5)
    driver.find_element(By.XPATH, "//button[@id='ACCOUNT']").click()
    sleep(5)
    driver.find_element(By.XPATH, "//a[normalize-space()='Log out']").click()
    sleep(5)
    # sleep(5)
    # driver.find_element(By.XPATH, "").click()
    # sleep(5)
