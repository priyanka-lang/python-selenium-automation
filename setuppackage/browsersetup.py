import pytest
from selenium.webdriver import Chrome
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
@pytest.yield_fixture()
def browser():
    # Initialize ChromeDriver
    print("open browser")
    firefox_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    firefox_driver.implicitly_wait(10)
    firefox_driver.maximize_window()

    yield firefox_driver
    print("close browser")
    firefox_driver.quit()

    # chrome_driver = webdriver.Chrome(ChromeDriverManager().install())
    # chrome_driver.implicitly_wait(10)
    # chrome_driver.maximize_window()
    #
    # yield chrome_driver
    # print("close browser")
    # chrome_driver.quit()




