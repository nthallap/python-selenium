import time
from selenium import webdriver

base_url = "https://google.co.in"
chrome_driver_path = r"C:\Users\nthallap\Downloads\drivers\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(base_url)
driver.implicitly_wait(10)
driver.set_page_load_timeout(20)
google_search = driver.find_element_by_xpath("//input[contains(@class, 'gLFyf')]")
print(google_search.is_enabled())
google_search.send_keys("Nageswara Rao Thallapalli")
driver.find_element_by_xpath("//input[@value='Google Search']").click()
driver.back()
time.sleep(3)

google_search = driver.find_element_by_xpath("//input[contains(@class, 'gLFyf')]")
google_search.send_keys("Good Morning")
driver.find_element_by_xpath("//input[@value='Google Search']").click()



