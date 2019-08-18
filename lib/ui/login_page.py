from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class LoginPage:
    def __init__(self,driver):
        self.driver=driver

    def wait_for_login_page_to_load(self):
        wait=WebDriverWait(self.driver, 30)
        wait.until(expected_conditions.visibility_of(self.get_email_textbox()))
        wait.until(expected_conditions.visibility_of(self.get_password_textbox()))
        wait.until(expected_conditions.visibility_of(self.get_login_btton()))


    def get_email_textbox(self):
        try:
            return self.driver.find_element_by_xpath('//input[@name="email"]')
        except:
            return None

    def get_password_textbox(self):
        try:
            return self.driver.find_element_by_xpath('//input[@name="password"]')
        except:
            return None

    def get_login_btton(self):
        try:
            return self.driver.find_element_by_xpath('//div[text()="Login"]')
        except:
            return None