import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *


def test_explicit_wait():
    driver = webdriver.Chrome()
    driver.get("https://www.letskodeit.com/practice")
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.set_page_load_timeout(60)

    wait = WebDriverWait(driver, 100, poll_frequency=10,
                         ignored_exceptions=[NoSuchElementException,
                                             ElementNotVisibleException, ElementNotInteractableException])
    element = driver.find_element(By.CSS_SELECTOR, 'a[id="opentab"]')

    link = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'a[id="opentab"]')))
    current_window = driver.current_window_handle
    link.click()

    all_windows = driver.window_handles

    driver.switch_to.window(all_windows[1])
    time.sleep(30)
    driver.switch_to.window(current_window)

    time.sleep(30)
    driver.quit()


