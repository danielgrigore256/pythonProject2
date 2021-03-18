from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

class main_page():


    def go_to_all_releases (driver):

        download_menu = driver.find_element_by_xpath("//li[@id='downloads']/a")
        all_releases_xpath = "//li[@id='downloads']/ul[@role='menu']/li[@class='tier-2 element-1']/a"
        all_releases_submenu = driver.find_element_by_xpath(all_releases_xpath)
        ActionChains(driver).move_to_element(download_menu).click(all_releases_submenu).perform()
        return driver

    def search_bar(driver, search_keys):

        search_bar = driver.find_element_by_id("id-search-field")
        search_bar.send_keys(search_keys)
        search_bar.send_keys(Keys.RETURN)
        time.sleep(5)
        return driver




