class LocGeneric:
    def __init__(self, driver):
        self.driver = driver

    def locator(self, loc_type, loc_value):
        try:

            if (loc_type == "name"):
                ele = self.driver.find_element_by_name(loc_value)
                return ele

            elif (loc_type == "id"):
                ele = self.driver.find_element_by_id(loc_value)
                return ele

            elif (loc_type == "class_name"):
                ele = self.driver.find_element_by_class_name(loc_value)
                return ele

            elif (loc_type == "xpath"):
                ele = self.driver.find_element_by_xpath(loc_value)
                return ele

        except AssertionError as e:
            print("report fail")

        except:
            print("fail")
