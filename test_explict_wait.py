import time
from basic import basic_setup
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *

base_url = "https://www.redbus.in/"


driver = basic_setup(base_url)
source_xpath = "//input[@id='src']"
dest_xpath = "//input[@id='dest']"
cal_xpath = "//input[@id='onward_cal']"
search_btn = "//button[@id='search_btn']"

driver.find_element(By.XPATH, source_xpath).send_keys("Guntur")
#driver.ffind_element(By.XPATH, "//li[contains(text(), 'Guntur')][1]")
wait = WebDriverWait(driver, 10, poll_frequency=1,
                     ignored_exceptions=[NoSuchElementException,
                                         ElementNotSelectableException,
                                         ElementNotSelectableException])
element = wait.until(ec.element_to_be_clickable((By.XPATH,"//li[contains(text(), 'Guntur')][1]")))
element.click()

driver.find_element(By.XPATH, dest_xpath).send_keys("Chennai")

dest_elem = wait.until(ec.element_to_be_clickable((By.XPATH,"//li[contains(text(), 'Chennai')][1]")))
dest_elem.click()

driver.find_element(By.XPATH, cal_xpath).click()
dates_xpath = "//table[contains(@class, 'rb-monthTable')]//td[contains(@class, 'current day') or contains(@class, 'wd day')]"
dates_elements = driver.find_elements(By.XPATH, dates_xpath)

for day_ele in dates_elements:
    if day_ele.text == "29":
        day_ele.click()
        break

driver.find_element(By.XPATH, search_btn).click()
time.sleep(10)
driver.quit()
