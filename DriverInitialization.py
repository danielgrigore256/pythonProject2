from selenium import webdriver


class DriverInitialization():
    Instance = None

    def Initialize(link):
        global Instance
        Instance = webdriver.Chrome('./chromedriver')
        Instance.implicitly_wait(5)
        Instance.get(link)
        return Instance