
from selenium.webdriver.common.by import By
from basic import basic_setup
base_url = "https://www.redbus.in/"

driver = basic_setup(base_url)

#print(dir(driver))
print(driver.capabilities["browserVersion"])
print(driver.capabilities["browserName"])
calender = driver.find_element(By.CSS_SELECTOR, "#onwardCal").click()
dates_xpath = "//table[contains(@class, 'rb-monthTable')]//td[contains(@class, 'current day') or contains(@class, 'wd day')]"
dates_elements = driver.find_elements(By.XPATH, dates_xpath)

for day_ele in dates_elements:
    print(day_ele.text)
    if day_ele.text == "27":
        day_ele.click()
        break

