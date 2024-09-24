
from selenium.webdriver.support.select import Select
from basic import basic_setup
import time

base_url = "https://google.co.in"


driver = basic_setup(base_url)
drop_down = driver.find_element_by_xpath("//select[@id='carselect']")
sel = Select(drop_down)
sel.select_by_index(2)
time.sleep(3)
sel.select_by_visible_text("BMW")
time.sleep(3)
sel.select_by_value("benz")
time.sleep(3)
sel.select_by_index('0')
driver.quit()
