from selenium.webdriver.common.keys import Keys
from selenium import webdriver


class python_search_page():
    def click_on_first_result(driver):

        link_xpath = "//ul[@class='list-recent-events menu']//a[@href='/dev/peps/pep-0318/']"
        link = driver.find_element_by_xpath(link_xpath)
        link.click()
        return driver
