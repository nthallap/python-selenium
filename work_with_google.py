import time
from basic import basic_setup
from selenium.webdriver.common.by import By

base_url = "https://google.co.in"

driver = basic_setup(base_url)
driver.get(base_url)
driver.implicitly_wait(10)
driver.set_page_load_timeout(20)
google_search = driver.find_element(By.XPATH, "(//textarea)[1]")
print(google_search.is_enabled())
google_search.send_keys("Nageswara Rao Thallapalli")
driver.find_element(By.XPATH, "(//input[@value='Google Search'])[2]").click()
driver.back()
time.sleep(3)

oogle_search = driver.find_element(By.XPATH, "(//textarea)[1]")
google_search.send_keys("Good Morning")
driver.find_element(By.XPATH, "(//input[@value='Google Search'])[2]").click()

