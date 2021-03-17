from selenium import webdriver

class Decorator():
    def decorator_function(original_function):
        """
        :parameter original_function : function u want to decorate
        :return: stores into a variable the given function
        """

        def wrapper_function():
            return original_function

        return wrapper_function()

    def close_driver(driver):
        """
        function to close the webdriver
        :return: None
        """
        driver.close()