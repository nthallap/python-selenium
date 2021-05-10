from selenium import webdriver
from selenium.webdriver.common.by import By

base_url = "https://www.redbus.in/"
chrome_driver_path = r"C:\Users\nthallap\Downloads\drivers\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)


driver.maximize_window()
driver.implicitly_wait(10)
driver.set_page_load_timeout(120)

driver.get(base_url)
#print(dir(driver))
print(driver.capabilities["browserVersion"])
print(driver.desired_capabilities["browserName"])
calender = driver.find_element_by_xpath("//input[@id='onward_cal']").click()
dates_xpath = "//table[contains(@class, 'rb-monthTable')]//td[contains(@class, 'current day') or contains(@class, 'wd day')]"
dates_elements = driver.find_elements(By.XPATH, dates_xpath)

for day_ele in dates_elements:
    print(day_ele.text)
    if day_ele.text == "27":
        day_ele.click()
        break

