from selenium.webdriver.common.keys import Keys
from selenium import webdriver


class SearchPage():
    def __init__(self, driver):
        self.driver = driver
    """
    The page after searching something in the search  bar of main python.org page
    """
    def click_on_first_result(self):
        """
        (TEST2) clicking on first result after searching something in search bar
        :return: browser gets to decorators_page
        """

        link_xpath = "//ul[@class='list-recent-events menu']//a[@href='/dev/peps/pep-0318/']"
        link = self.driver.find_element_by_xpath(link_xpath)
        link.click()

