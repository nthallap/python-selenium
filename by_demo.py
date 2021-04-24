from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r"C:\Users\nthallap\Downloads\drivers\chromedriver.exe")

driver.get("https://letskodeit.teachable.com/p/practice")
print(driver.current_url)

drop_down = driver.find_element(By.XPATH, "//select[@id='carselect']")

print("***below is the dropdown")
print(drop_down)
driver.close()