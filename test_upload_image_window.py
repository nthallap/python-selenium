import time

from selenium.webdriver.common.by import By
from pynput.keyboard import Key, Controller
from pathlib import Path
from basic import basic_setup, root_path


def test_upload_file():
    driver = basic_setup("https://plupload.com/examples/")
    keyword = Controller()
    file_path = Path(root_path).joinpath("test_data").joinpath("myscreen_shot.png")
    driver.find_element(By.ID, "uploader_browse").click()
    time.sleep(5)
    print(file_path)
    keyword.type(str(file_path))
    keyword.press(key=Key.enter)
    keyword.release(key=Key.enter)
    driver.find_element(By.ID, 'uploader_start').click()
    time.sleep(5)
    driver.close()

