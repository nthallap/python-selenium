from selenium import webdriver
import time
base_url = "https://letskodeit.teachable.com"
chrome_driver_path = r"C:\Users\nthallap\Downloads\drivers\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.maximize_window()
driver.implicitly_wait(5)
driver.set_page_load_timeout(30)
driver.get(base_url)
driver.find_element_by_xpath("//a[contains(text(),'Practice')]").click()
time.sleep(5)
print("after click page url", driver.current_url)
driver.back()
#print(driver.page_source)
print(driver.title)
driver.save_screenshot("my_screenshot.png")
print("after back page url", driver.current_url)
driver.forward()
driver.refresh()
print("after forward page url", driver.current_url)
driver.quit()

