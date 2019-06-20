import pytest

from selenium import webdriver
from data.jenkins_data import *


@pytest.fixture(scope='class')
def test_launch_browser_and_application(request):
    global driver
    driver = webdriver.Chrome(executable_path=MY_CHROME_PATH)
    driver.get(JENKINS_URL)
    driver.maximize_window()
    driver.implicitly_wait(20)

    request.cls.driver = driver

    yield
    driver.quit()
