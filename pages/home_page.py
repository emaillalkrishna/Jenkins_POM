from pages.jenkins_webgeneric import WebGeneric


class Logout(WebGeneric):
    def __init__(self, driver):
        WebGeneric.__init__(self, driver)
        self.driver = driver
        self.logoutbutton_by_xpath = "//*[text()='log out']"

        global wg
        wg = WebGeneric(driver)

    def click_on_logout(self):
        # self.driver.find_element_by_xpath(self.logoutbutton_by_xpath).click()
        wg.click_button("xpath", self.logoutbutton_by_xpath)
