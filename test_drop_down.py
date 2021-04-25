from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

base_url = "https://google.co.in"
chrome_driver_path = r"C:\Users\nthallap\Downloads\drivers\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.implicitly_wait(10)
driver.set_page_load_timeout(30)

driver.get("https://letskodeit.teachable.com/p/practice")
driver.maximize_window()

drop_down = driver.find_element_by_xpath("//select[@id='carselect']")
sel = Select(drop_down)
sel.select_by_index(2)
time.sleep(3)
sel.select_by_visible_text("BMW")
time.sleep(3)
sel.select_by_value("benz")
time.sleep(3)
sel.select_by_index(0)
driver.quit()
