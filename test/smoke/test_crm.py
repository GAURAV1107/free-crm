import unittest
from lib.ui.home_page import HomePage
from lib.ui.login_page import LoginPage
from lib.ui.logout_page import LogOut
from lib.utils import create_driver

class TestComponent(unittest.TestCase):
    def setUp(self):
        self.driver= create_driver.get_driver_instance()
        self.home=HomePage(self.driver)
        self.login=LoginPage(self.driver)
        self.logout=LogOut(self.driver)


    def tearDown(self):
        self.driver.close()

    def test_framework_component(self):
        self.home.wait_for_home_page_to_load()
        self.home.get_login_button().click()
        self.login.wait_for_login_page_to_load()
        self.login.get_email_textbox().send_keys('gauravsingh1107@gmail.com')
        self.login.get_password_textbox().send_keys('Mgaurav1107')
        self.login.get_login_btton().click()
        self.logout.get_setting_button().click()
        self.logout.get_logout_button().click()
