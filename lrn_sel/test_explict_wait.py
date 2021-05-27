import time


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *

base_url = "https://www.redbus.in/"
chrome_driver_path = r"C:\Users\nthallap\Downloads\drivers\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(base_url)

driver.maximize_window()
driver.set_page_load_timeout(20)

source_xpath = "//input[@id='src']"
dest_xpath = "//input[@id='dest']"
cal_xpath = "//input[@id='onward_cal']"
search_btn = "//button[@id='search_btn']"

driver.find_element_by_xpath(source_xpath).send_keys("Guntur")
#driver.find_element_by_xpath("//li[contains(text(), 'Guntur')][1]")
wait = WebDriverWait(driver, 10, poll_frequency=1,
                     ignored_exceptions=[NoSuchElementException,
                                         ElementNotSelectableException,
                                         ElementNotSelectableException])
element = wait.until(ec.element_to_be_clickable((By.XPATH,"//li[contains(text(), 'Guntur')][1]")))
element.click()

driver.find_element_by_xpath(dest_xpath).send_keys("Chennai")

dest_elem = wait.until(ec.element_to_be_clickable((By.XPATH,"//li[contains(text(), 'Chennai')][1]")))
dest_elem.click()

driver.find_element_by_xpath(cal_xpath).click()
dates_xpath = "//table[contains(@class, 'rb-monthTable')]//td[contains(@class, 'current day') or contains(@class, 'wd day')]"
dates_elements = driver.find_elements(By.XPATH, dates_xpath)

for day_ele in dates_elements:
    if day_ele.text == "29":
        day_ele.click()
        break

driver.find_element_by_xpath(search_btn).click()
time.sleep(10)
driver.quit()