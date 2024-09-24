
from selenium.webdriver.common.by import By
from basic import basic_setup

driver = basic_setup()

print(driver.current_url)

drop_down = driver.find_element(By.XPATH, "//select[@id='carselect']")
tag_list = driver.find_elements(By.TAG_NAME,"input")
print("***below is the dropdown")
print(drop_down)

print("below is the list of input tags")
print(tag_list)
driver.close()


# we have below clasesses in By class. we can use all of them
# ID = "id"
# XPATH = "xpath"
# LINK_TEXT = "link text"
# PARTIAL_LINK_TEXT = "partial link text"
# NAME = "name"
# TAG_NAME = "tag name"
# CLASS_NAME = "class name"
# CSS_SELECTOR = "css selector"
