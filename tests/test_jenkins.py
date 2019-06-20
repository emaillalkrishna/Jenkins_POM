import pytest

from pages.login_page import Login
from pages.home_page import Logout


@pytest.mark.usefixtures("test_launch_browser_and_application")
class Test_JenkinLoginLogout:

    def test_login_jenkins(self):
        driver = self.driver
        lp = Login(driver)
        lp.enter_user_name()
        lp.enter_password()
        lp.click_signin_button()

    def test_logout_jenkins(self):
        driver = self.driver
        hp = Logout(driver)
        hp.click_on_logout()
