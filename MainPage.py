from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

class MainPage():
    """
    instance of maine page python.org
    """
    def __init__(self, driver):
        self.driver = driver


    def go_to_all_releases (self):
        """
        (TEST1): automated path to click Downloads - > All Releases
        :return: Opening the releases_page
        """

        download_menu = self.driver.find_element_by_xpath("//li[@id='downloads']/a")
        all_releases_xpath = "//li[@id='downloads']/ul[@role='menu']/li[@class='tier-2 element-1']/a"
        all_releases_submenu = self.driver.find_element_by_xpath(all_releases_xpath)
        ActionChains(self.driver).move_to_element(download_menu).click(all_releases_submenu).perform()


    def use_search_bar(self):
        """
        (TEST2) Function to use python.org search bar in order to write something and display results
        :return: moving to python_search_page with the display of results searched
        """

        search_bar = self.driver.find_element_by_id("id-search-field")
        search_bar.send_keys('decorator')
        search_bar.send_keys(Keys.RETURN)
        time.sleep(5)





