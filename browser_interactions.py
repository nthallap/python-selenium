import time
from basic import basic_setup, root_path
from selenium.webdriver.common.by import By
from pathlib import Path

driver = basic_setup("https://letskodeit.teachable.com/p/practice")
element = driver.find_element(By.CSS_SELECTOR, 'a[href="https://www.letskodeit.com/practice"]')
href = element.get_attribute('href')
print("href=", href)
element.click()
time.sleep(5)
print("after click page url", driver.current_url)
driver.back()

#print(driver.page_source)
print(driver.title)
file_path = Path(root_path).joinpath("test_data").joinpath("myscreen_shot.png")
file_path2 = Path(root_path).joinpath("test_data").joinpath("myscreen_shot2.png")
print(file_path2, file_path)
driver.save_screenshot(file_path)
driver.get_screenshot_as_file(file_path2)
print("after back page url", driver.current_url)
driver.forward()
driver.refresh()
print("after forward page url", driver.current_url)


driver.quit()

