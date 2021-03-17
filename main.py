from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import time



class RunChrome:

    def test1(self,link):
        """
        test sequence 1
        """
        # 1. driver initialization and opening Chrome Browser
        driver = webdriver.Chrome('./chromedriver')
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(link)

        # 2. Going to Downloads -> All Releases
        download_menu = driver.find_element_by_xpath("//li[@id='downloads']/a")
        all_releases_xpath = "//li[@id='downloads']/ul[@role='menu']/li[@class='tier-2 element-1']/a"
        all_releases_submenu = driver.find_element_by_xpath(all_releases_xpath)
        ActionChains(driver).move_to_element(download_menu).click(all_releases_submenu).perform()

        # 3. Printing the last version of python
        all_versions_xpath = "//ol[@class='list-row-container menu']/li/span[@class='release-number']/a"
        all_versions = driver.find_elements_by_xpath(all_versions_xpath)
        time.sleep(3)
        print(all_versions[0].text)

    def test2(self, link):
            """
            test sequence 1
            """
            # 1. driver initialization and opening Chrome Browser
            driver = webdriver.Chrome('./chromedriver')
            driver.maximize_window()
            driver.implicitly_wait(10)
            driver.get(link)

            # 2. Search bar
            search_bar = driver.find_element_by_id("id-search-field")
            search_bar.send_keys("decorator")
            search_bar.send_keys(Keys.RETURN)
            time.sleep(5)

            # 3. Open first result link





chromeTest = RunChrome()
chromeTest.test1("https://www.python.org/")
