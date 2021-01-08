from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

import time


url = "https://westores.online/login"

driver = webdriver.Firefox(executable_path="geckodriver.exe")

driver.get(url)
assert "Login" in driver.title

# driver.execute_script("window.scrollTo(0,1000);")

time.sleep(5)

email = input("Please enter your username: \n")
password = input("Please enter your password: \n")
email_field = driver.find_element_by_name("email")
pass_field = driver.find_element_by_name("pass")
email_field.clear()
email_field.send_keys(email)
time.sleep(3)
pass_field.clear()
pass_field.send_keys(password)
time.sleep(3)
driver.find_element_by_name("submit").click()

time.sleep(15)


# iframe = driver.find_element_by_id("#csr")
# driver.switch_to.frame(iframe)
# my_stores = driver.find_element_by_xpath("/html/body/div[2]/header/div/div/div[1]/div[5]/div/nav/ul/li[3]/a")
product_tab = driver.find_element_by_xpath("/html/body/div[2]/header/div/div/div[1]/div[5]/div/nav/ul/li[2]/a").click()
# hover = ActionChains(driver).move_to_element(my_stores)
# hover.perform()
# time.sleep(1)
# driver.find_element_by_link_text("F.a.online").click()
