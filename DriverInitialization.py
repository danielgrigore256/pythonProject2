from selenium import webdriver


class DriverInitialization():
    instance = None
    """
    creating an instance of the webdriver chrome that will be used in test scripts
    """
    def initialize_driver(link):
        global instance
        instance = webdriver.Chrome('./chromedriver')
        instance.implicitly_wait(5)
        instance.get(link)
        return instance