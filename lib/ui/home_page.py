from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class HomePage:
    def __init__(self,driver):
        self.driver=driver

    def wait_for_home_page_to_load(self):
        wait=WebDriverWait(self.driver,30)
        wait.until(expected_conditions.visibility_of(self.get_login_button()))
        wait.until(expected_conditions.visibility_of(self.get_signup_button()))


    def get_login_button(self):
        try:
            return self.driver.find_element_by_link_text('Login')
        except:
            return None

    def get_signup_button(self):
        try:
            return self.driver.find_element_by_xpath('//li[a[text()="Sign Up"]]')
        except:
            return None