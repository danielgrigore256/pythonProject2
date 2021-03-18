from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

class main_page():
    """
    instance of maine page python.org
    """


    def go_to_all_releases (driver):
        """
        (TEST1): automated path to click Downloads - > All Releases
        :return: Opening the releases_page
        """

        download_menu = driver.find_element_by_xpath("//li[@id='downloads']/a")
        all_releases_xpath = "//li[@id='downloads']/ul[@role='menu']/li[@class='tier-2 element-1']/a"
        all_releases_submenu = driver.find_element_by_xpath(all_releases_xpath)
        ActionChains(driver).move_to_element(download_menu).click(all_releases_submenu).perform()
        return driver

    def search_bar(driver, search_keys):
        """
        (TEST2) Function to use python.org search bar in order to write something and display results
        :param search_keys: the string u want to search on the search bar, "decorator" for our test case
        :return: moving to python_search_page with the display of results searched
        """

        search_bar = driver.find_element_by_id("id-search-field")
        search_bar.send_keys(search_keys)
        search_bar.send_keys(Keys.RETURN)
        time.sleep(5)
        return driver




