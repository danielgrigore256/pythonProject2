from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from DriverInitialization import DriverInitialization
from main_page import main_page
from releases_page import releases_page
from python_search_page import python_search_page
from decorators_page import decorators_page
import time


def decorated_close(test):
    def wrapper(*args):
        driver = test(*args)
        driver.close()
        print("driver closed")

    return wrapper


class RunChrome:

    @decorated_close
    def test1(self):
        """
        test sequence 1
        """

        # 1. Driver Initialization
        initialization_object = DriverInitialization
        driver = initialization_object.Initialize("https://www.python.org/")

        # 2. Going to Downloads -> All Releases
        driver = main_page.go_to_all_releases(driver)

        # 3. Printing the last version of python
        driver = releases_page.display_last_release(driver)

        return driver

    @decorated_close
    def test2(self):
        """
        test sequence 1
         """
        # 1. driver initialization and opening Chrome Browser
        initialization_object = DriverInitialization
        driver = initialization_object.Initialize("https://www.python.org/")

        # 2. Search bar
        driver = main_page.search_bar(driver, "decorator")

        # 3. Open first result link
        driver = python_search_page.click_on_first_result(driver)

        # 4. Select Examples
        driver = decorators_page.select_examples(driver)

        # 5. Verify current example count is 5
        driver = decorators_page.verify_examples_count(driver)

        return driver


chromeTest = RunChrome()
chromeTest.test2()
