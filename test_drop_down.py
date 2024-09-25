
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from basic import basic_setup
import time

driver = basic_setup()
drop_down = driver.find_element(By.XPATH, "//select[@id='carselect']")
sel = Select(drop_down)
sel.select_by_index(2)
time.sleep(3)
sel.select_by_visible_text("BMW")
time.sleep(3)
sel.select_by_value("benz")
time.sleep(3)
sel.select_by_index('0')
driver.quit()
