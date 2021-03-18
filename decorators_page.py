class decorators_page():
    """
    python org webpage that display the PEP tutorial for Decorators
    This page is used for last part of test 2
    """

    def select_examples(driver):
        """
        :return: the examples chapter in the Decorators documentation page
        """
        examples_link = driver.find_element_by_id("id80")
        examples_link.click()
        return driver

    def verify_examples_count(driver):
        """
        function to store the number of webelements that contains examples and count them
        :return: True if there are 5 elements / False otherwise
        """
        examples_list_xpath = "//div[@id='examples']/ol[@class='arabic']/li/p[@class='first']"
        examples_list = driver.find_elements_by_xpath(examples_list_xpath)
        if len(examples_list) == 5:
            check = True
        else:
            check = False
        print("Are there 5 examples? " + str(check))
        return driver
