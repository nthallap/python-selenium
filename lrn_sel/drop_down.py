from lrn_sel.basic import basic_setup
from selenium.webdriver import ActionChains
import time

base_url = "https://jqueryui.com/droppable/"

driver = basic_setup(base_url)

actions = ActionChains(driver)

driver.switch_to.frame(0)

time.sleep(2)
dragable = driver.find_element_by_xpath("//div[@id='draggable']")
dropable = driver.find_element_by_xpath("//div[@id='droppable']")

#actions.drag_and_drop(dragable,dropable).perform()
actions.click_and_hold(dragable).move_to_element(dropable).release().perform()

driver.close()