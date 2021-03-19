from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from DriverInitialization import DriverInitialization
from MainPage import MainPage
from ReleasesPage import ReleasesPage
from SearchPage import SearchPage
from DecoratorsPage import DecoratorsPage
import time


def decorated_close(test):
    def wrapper(*args):
        driver = test(*args)
        driver.driver.close()
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
        driver = initialization_object.initialize_driver("https://www.python.org/")

        # 2. Going to Downloads -> All Releases

        driver = MainPage(driver)
        driver.go_to_all_releases()

        # 3. Printing the last version of python
        driver = ReleasesPage(driver)
        driver.display_last_release
        return driver.driver

    @decorated_close
    def test2(self):
        """
        test sequence 1
         """
        # 1. driver initialization and opening Chrome Browser
        initialization_object = DriverInitialization
        driver = initialization_object.initialize_driver("https://www.python.org/")

        # 2. Search bar
        main_page_driver = MainPage(driver)
        main_page_driver.use_search_bar()

        # 3. Open first result link
        search_page_driver = SearchPage(main_page_driver.driver)
        search_page_driver.click_on_first_result()

        # 4. Select Examples
        decorator_page_driver = DecoratorsPage(search_page_driver.driver)
        decorator_page_driver.select_examples()
        # 5. Verify current example count is 5
        decorator_page_driver.verify_examples_count()

        return decorator_page_driver


chromeTest = RunChrome()
chromeTest.test2()
