import time

from basic import basic_setup
from selenium.webdriver.common.by import By


def test_switch_to_alert():
    driver = basic_setup()
    driver.find_element(By.ID, 'name').send_keys("Nageswara Rao")
    driver.find_element(By.ID, 'alertbtn').click()
    time.sleep(5)
    alert = driver.switch_to.alert
    time.sleep(5)
    # alert.accept()
    alert.dismiss()
    time.sleep(10)

