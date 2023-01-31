from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def test_run():
    print("starting...")

    # create webdriver object
    driver = webdriver.Chrome('D:\\Downloads\\chromedriver_win32 (1).exe')
    # get (google.co.in)
    driver.get("https://google.com/")
    driver.maximize_window()
    driver.find_element(By.NAME, "q").send_keys("geeksforgeeks")
    driver.find_element(
        By.XPATH, "//div[@class='FPdoLc lJ9FBc']//input[@name='btnK']").send_keys(Keys.ENTER)
    driver.find_element(
        By.XPATH, "//h3[contains(text(),'GeeksforGeeks | A computer science portal for geek')]").click()
    driver.find_element(
        By.XPATH, "//a[@href='https://www.geeksforgeeks.org/python-programming-language/?ref=shm']").click()

    print(driver.current_url)
    driver.close()
    print("Success")
