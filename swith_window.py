import time

from selenium.webdriver.common.by import By
from basic import basic_setup
from selenium.webdriver.common.keys import Keys


driver = basic_setup()


# practice_page = "//a[contains(text(),'Practice')]"
# driver.find_element(By.XPATH, practice_page).click()
# time.sleep(5)

parent_handler = driver.current_window_handle
print("parent window handler", parent_handler)
open_window = "//button[@id='openwindow']"
new_window_element = driver.find_element(By.XPATH, open_window)
new_window_element.click()

all_handlers = driver.window_handles

for hand in all_handlers:
    print(hand)

driver.switch_to.window(all_handlers[1])
print(driver.current_url)
time.sleep(5)
driver.switch_to.window(parent_handler)
print(driver.current_url)

driver.quit()
