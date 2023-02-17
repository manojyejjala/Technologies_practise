# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import Select

# def test_run():
#     print("Starting......")
#     driver = webdriver.Chrome()
#     driver.get("http://139.59.79.118/")
#     driver.maximize_window()
#     # status button check
#     driver.find_element(By.XPATH, "//a[normalize-space()='Status']").click()
#     # search box check
#     driver.find_element(By.XPATH, "//input[@type='search']").send_keys("manoj")
#     # back link check
#     driver.find_element(By.XPATH, "//a[normalize-space()='<-Back']").click()
#     # mytablelenght dropdown check
#     driver.find_element(By.XPATH, "//a[normalize-space()='Status']").click()
#     Select(driver.find_element(
#         By.XPATH, "//select[@name='myTable_length']")).select_by_index(2)
#     driver.find_element(By.XPATH, "//a[normalize-space()='<-Back']").click()
#     # '2' link check
#     driver.find_element(By.XPATH, "//a[normalize-space()='Status']").click()
#     driver.find_element(By.XPATH, "//a[normalize-space()='2']").click()
#     # previous page button check
#     driver.find_element(By.XPATH, "//a[normalize-space()='Previous']").click()
#     # next page button check
#     driver.find_element(By.XPATH, "//a[normalize-space()='Next']").click()
#     driver.find_element(By.XPATH, "//a[normalize-space()='<-Back']").click()
#     # stat link check
#     driver.find_element(By.XPATH, "//a[normalize-space()='Stat']").click()
#     # home button check
#     driver.find_element(By.XPATH, "//a[normalize-space()='Home']").click()
#     # heading on home page
#     # driver.find_element(By.XPATH, "//nav[@class='navbar navbar-expand-sm bg-dark navbar-dark']")
#     driver.find_element(By.XPATH, "//p[normalize-space()='Director : Ashok Nalla']")
#     print(('hiiiiii'))
#     # print(driver.find_element(By.CLASS_NAME, 'w3-display-middle w3-large'))





from selenium import webdriver
#set chromodriver.exe path
driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
driver.implicitly_wait(0.5)
#launch URL
driver.get("https://www.tutorialspoint.com/tutor_connect/index.php")
#Select class for dropdown
l= driver.find_element_by_name("selType")
d= Select(l)
print('Options are: ')
#iterate over dropdown options
for opt in d.options:
#get option text
   print(opt.text)
#browser quit
driver.quit()