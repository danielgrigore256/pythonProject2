from selenium.webdriver.common.by import By


class FindElements():

    """
    class that simplify in main code the procedure of finding browser elements
    """
    def __init__(self, driver):
        self.driver = driver



    @staticmethod
    def get_type(locatorType):

        """
        Method to convert the type of path selected to find element into the By.TYPE input of find_element method
        :param locatorType: a string with the type of path given to find element
        :return: By.<Type>
        """

        if locatorType == "id":
            return By.ID
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "class_name" or locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "css_selector":
            return By.CSS_SELECTOR
        elif locatorType == "link_text" or locatorType == "link":
            return By.LINK_TEXT
        elif locatorType == "tag_name" or locatorType == "tag":
            return By.TAG_NAME
        elif locatorType == "partial_link_text":
            return By.PARTIAL_LINK_TEXT
        else:
            print("Locator type is not supported")
        return False

    def get_element(self, locatorType, locator):
        """

        :param self:
        :param locatorType: string that specify type of path given ("id", "class", "css", etc)
        :param locator: the actual path to the web page element
        :return: the element requested if found, if not an error message
        """
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.get_type(locatorType)
            element = self.driver.find_element(byType, locator)
            print("Element Found")

        except:
            print("Element not Found")

        return element




