from selenium import webdriver


class DriverInitialization():
    Instance = None
    """
    creating an instance of the webdriver chrome that will be used in test scripts
    """
    def Initialize(link):
        global Instance
        Instance = webdriver.Chrome('./chromedriver')
        Instance.implicitly_wait(5)
        Instance.get(link)
        return Instance