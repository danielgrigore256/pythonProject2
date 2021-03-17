from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from DriverInitialization import DriverInitialization
import time


class RunChrome:

    def test1(self, link):
        """
        test sequence 1
        """

        # 1. Driver Initialization
        initialization_object = DriverInitialization
        driver = initialization_object.Initialize(link)

        # 2. Going to Downloads -> All Releases
        download_menu = driver.find_element_by_xpath("//li[@id='downloads']/a")
        all_releases_xpath = "//li[@id='downloads']/ul[@role='menu']/li[@class='tier-2 element-1']/a"
        all_releases_submenu = driver.find_element_by_xpath(all_releases_xpath)
        ActionChains(driver).move_to_element(download_menu).click(all_releases_submenu).perform()

        # 3. Printing the last version of python
        all_versions_xpath = "//ol[@class='list-row-container menu']/li/span[@class='release-number']/a"
        all_versions = driver.find_elements_by_xpath(all_versions_xpath)
        time.sleep(3)
        print("The latest released version is : " + str(all_versions[0].text))

        # Extra 1 : decorator function to close drive
        decorated_close = RunChrome.decorator_function(RunChrome.close_driver)
        decorated_close(driver)

    def test2(self, link):
        """
        test sequence 1
         """
        # 1. driver initialization and opening Chrome Browser
        initialization_object = DriverInitialization
        driver = initialization_object.Initialize(link)

        # 2. Search bar
        search_bar = driver.find_element_by_id("id-search-field")
        search_bar.send_keys("decorator")
        search_bar.send_keys(Keys.RETURN)
        time.sleep(5)

        # 3. Open first result link
        link_xpath = "//ul[@class='list-recent-events menu']//a[@href='/dev/peps/pep-0318/']"
        link = driver.find_element_by_xpath(link_xpath)
        link.click()

        # 4. Select Examples
        examples_link = driver.find_element_by_id("id80")
        examples_link.click()

        # 5. Verify current example count is 5
        examples_list_xpath = "//div[@id='examples']/ol[@class='arabic']/li/p[@class='first']"
        examples_list = driver.find_elements_by_xpath(examples_list_xpath)
        if len(examples_list) == 5:
            check = True
        else:
            check = False
        print("Are there 5 examples? " + str(check))

        # Extra 1 : decorator function to close drive
        decorated_close = RunChrome.decorator_function(RunChrome.close_driver)
        decorated_close(driver)

    def decorator_function(original_function):
        """
        :parameter original_function : function u want to decorate
        :return: stores into a variable the given function
        """
        def wrapper_function():
            return original_function
        return wrapper_function()

    def close_driver(driver):
        """
        function to close the webdriver
        :return: None
        """
        driver.close()

chromeTest = RunChrome()
chromeTest.test2("https://www.python.org/")
