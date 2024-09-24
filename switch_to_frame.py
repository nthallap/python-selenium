import time
from lrn_sel.basic import basic_setup
from selenium.webdriver.common.by import By

driver = basic_setup()
# practice_page = "//a[contains(text(),'Practice')]"
# driver.find_element(By.XPATH, practice_page).click()
# time.sleep(5)

window_height = driver.execute_script("return window.innerHeight;")
window_width = driver.execute_script("return window.innerWidth")
page_height = driver.execute_script("return document.body.clientHeight")
print(window_width, window_height, page_height)

driver.execute_script("window.scrollBy(0,0);")
driver.execute_script("window.scrollBy(0, 1000);")

driver.switch_to.frame("courses-iframe")
driver.find_element(By.XPATH, "//input[@id='search']").send_keys("Python course")
time.sleep(3)

driver.switch_to.default_content()
driver.execute_script("window.scrollBy(0,0);")
driver.find_element(By.XPATH, "//input[@id='name']").send_keys("Good Morning")
time.sleep(2)

driver.find_element(By.XPATH, "//input[@id='alertbtn']").click()
# driver.switch_to_alert().accept()

alt = driver.switch_to.alert
print(alt.text)
alt.accept()


time.sleep(2)
driver.quit()
