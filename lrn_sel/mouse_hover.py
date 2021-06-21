import time

from lrn_sel.basic import basic_setup
from selenium.webdriver import ActionChains

base_url = "https://courses.letskodeit.com/practice"
mouse_hover = "//div[@class='mouse-hover']"
driver = basic_setup(base_url)

driver.execute_script("window.scrollBy(0,700);")
time.sleep(3)
element = driver.find_element_by_xpath(mouse_hover)
action = ActionChains(driver)
action.move_to_element(element).perform()

top_link = "//a[contains(text(),'Top')]"
top = driver.find_element_by_xpath(top_link)

action.click(top).perform()
time.sleep(2)
driver.quit()