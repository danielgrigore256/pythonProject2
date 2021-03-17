from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import time
from FindingElements import FindElements


class RunChrome:

    def test(self):
        """
        test sequence
        """
        # 1. driver initialization and opening Chrome Browser
        base_url = "https://www.python.org/"
        driver = webdriver.Chrome('./chromedriver')
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(base_url)

        python_browser = FindElements(driver)

        # 2. Going to Downloads -> All Releases
        download_menu = python_browser.get_element("xpath", "//li[@id='downloads']/a")
        all_releases_xpath = "//li[@id='downloads']/ul[@role='menu']/li[@class='tier-2 element-1']/a"
        all_releases_submenu = python_browser.get_element("xpath", all_releases_xpath)
        ActionChains(driver).move_to_element(download_menu).click(all_releases_submenu).perform()

        # 3. Printing the last version of python
        latest_version_xpath = "//ol[@class='list-row-container menu']/li[1]/span[@class='release-number']/a"
        latest_version = python_browser.get_element("xpath", latest_version_xpath)
        time.sleep(3)
        print(latest_version.text)


chromeTest = RunChrome()
chromeTest.test()
