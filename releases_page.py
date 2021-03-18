from selenium.webdriver.common.keys import Keys
import time

class releases_page():
    """
    Webpage tha appears after clicking Download -> All releases from main python.org page
    """

    def display_last_release(driver):
        """
        (TEST1) Display the latest version of python
        :return: print the last version on console (e.g. : " Python 2.5.3" )
        """

        all_versions_xpath = "//ol[@class='list-row-container menu']/li/span[@class='release-number']/a"
        all_versions = driver.find_elements_by_xpath(all_versions_xpath)
        time.sleep(3)
        print("The latest released version is : " + str(all_versions[0].text))
        return driver
