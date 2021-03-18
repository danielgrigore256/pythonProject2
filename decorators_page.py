class decorators_page():

    def select_examples(driver):
        examples_link = driver.find_element_by_id("id80")
        examples_link.click()
        return driver

    def verify_examples_count(driver):
        examples_list_xpath = "//div[@id='examples']/ol[@class='arabic']/li/p[@class='first']"
        examples_list = driver.find_elements_by_xpath(examples_list_xpath)
        if len(examples_list) == 5:
            check = True
        else:
            check = False
        print("Are there 5 examples? " + str(check))
        return driver
