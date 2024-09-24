from selenium import webdriver
from pathlib import Path
base_url = "https://www.letskodeit.com/practice"

root_path = Path(__file__).parent.parent

def basic_setup(url=base_url):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.set_page_load_timeout(60)
    driver.implicitly_wait(10)
    driver.get(url)
    return driver


if __name__ == "__main__":
    basic_setup()
    print(root_path)
