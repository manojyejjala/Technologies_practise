from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


def test_run():
    print("starting . . . . . . . . ")
    driver = webdriver.Chrome()
    driver.get(
        "https://www.tutorialspoint.com/selenium/selenium_automation_practice.htm")
    driver.maximize_window()
    # list_options = driver.find_element(By.XPATH, "//select[@name='continents']")
    # countries = [x.text for x in list_options.find_element_by_tag_name("tr")]
    # print(countries)

    # driver.execute_script("""(document.querySelector(//select[@name='continents']//option).text = 'India')""")

    driver.execute_script(
        """(document.querySelector("select[name='continents'] option").text = ' ')""")

    driver.execute_script(
        """(document.querySelector("select[name='continents'] option").text = ' ')""")

    l = driver.find_element(By.XPATH, "//select[@name='continents']")
    j = Select(l)
    # j.select_by_index(2)
    # options = [x for x in l.find_element(By.TAG_NAME, "option")]
    options = j.options

    # y = (options == [x for x in j.options()])

    q = [element.text for element in options]
    # for element in options:
    #     q = q + [element.text]
    print(q)

    # var x = document.createElement("OPTION")
    # var x = document.labelElement("India")

    print("end........")

    # for opt in j.options:
    #     print(opt.text)
    # d = l.find_elements_by_tag_name("tr")
    # for i in range(7):
    #     entries =d[i].find_elements_by_tag_name("th").text
    #     print(entries)
    # x = []
    # for opt in d.options:
    #     print(opt.text)

    time.sleep(20)


test_run()
