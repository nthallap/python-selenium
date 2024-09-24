import time

from selenium.webdriver.common.by import By

from lrn_sel.basic import basic_setup
from selenium.webdriver import ActionChains


mouse_hover = "//div[@class='mouse-hover']"
driver = basic_setup()

driver.execute_script("window.scrollBy(0,700);")
time.sleep(3)
element = driver.find_element(By.XPATH, mouse_hover)
action = ActionChains(driver)
action.move_to_element(element).perform()

top_link = "//a[contains(text(),'Top')]"
top = driver.find_element(By.XPATH, top_link)

action.click(top).perform()
time.sleep(2)
driver.quit()