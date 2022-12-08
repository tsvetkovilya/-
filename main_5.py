import time

from selenium import webdriver
driver = webdriver.Edge()
driver.get("https://adminqa.neapro.site/login")
driver.find_element("xpath", "//input[@id='admin_email']").click()
driver.find_element("xpath", "//input[@id='admin_email']").send_keys("blackleprosy@gmail.com")
driver.find_element("xpath", "//input[@id='admin_password']").click()
driver.find_element("xpath", "//input[@id='admin_password']").send_keys("123456789")
driver.find_element("xpath", "//input[@name='commit']").click()

time.sleep(5)