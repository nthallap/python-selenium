from selenium import webdriver

base_url = "https://letskodeit.teachable.com"
chrome_driver_path = r"C:\Users\nthallap\Downloads\drivers\chromedriver.exe"


def basic_setup(url=base_url):
    driver = webdriver.Chrome(chrome_driver_path)
    driver.maximize_window()
    driver.set_page_load_timeout(60)
    driver.implicitly_wait(10)
    driver.get(url)
    return driver
