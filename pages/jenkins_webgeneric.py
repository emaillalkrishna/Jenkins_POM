from pages.jenkins_locgeneric import LocGeneric

class WebGeneric(LocGeneric):
    def __init__(self, driver):
        LocGeneric.__init__(self,driver)
        self.driver = driver

        global lg
        lg = LocGeneric(driver)

    def enter_value(self, loc_type, loc_value, data):
        # self.driver.find_element_by_name(loc).send_keys(data)
        lg.locator(loc_type, loc_value).send_keys(data)



    def click_button(self, loc_type, loc_value):
        # self.driver.find_element_by_name(loc).click()
        # self.driver.find_element_by_xpath(loc).click()
        lg.locator(loc_type, loc_value).click()






