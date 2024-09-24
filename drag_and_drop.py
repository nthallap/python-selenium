from lrn_sel.basic import basic_setup
from selenium.webdriver import ActionChains
import time

base_url = "https://jqueryui.com/droppable/"

driver = basic_setup(base_url)

actions = ActionChains(driver)

driver.switch_to.frame(0)

time.sleep(2)
draggable = driver.find_element_by_xpath("//div[@id='draggable']")
droppable = driver.find_element_by_xpath("//div[@id='droppable']")


#actions.drag_and_drop(dragable,dropable).perform()
actions.click_and_hold(draggable).move_to_element(droppable).release().perform()

driver.close()
