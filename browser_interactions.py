import time
from basic import basic_setup, root_path
from selenium.webdriver.common.by import By
from pathlib import Path

driver = basic_setup("https://letskodeit.teachable.com/p/practice")
driver.find_element(By.CSS_SELECTOR, 'a[href="https://www.letskodeit.com/practice"]').click()

time.sleep(5)
print("after click page url", driver.current_url)
driver.back()

#print(driver.page_source)
print(driver.title)
file_path = Path(root_path).joinpath("test_data").joinpath("myscreen_shot.png")
driver.save_screenshot(file_path)
print("after back page url", driver.current_url)
driver.forward()
driver.refresh()
print("after forward page url", driver.current_url)
driver.quit()

