from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class LogOut:
    def __init__(self,driver):
        self.driver=driver


    def wait_for_logout_pagge_to_load(self):
        wait=WebDriverWait(self.driver,30)
        wait.until(expected_conditions.visibility_of(self.get_setting_button()))
        wait.until(expected_conditions.visibility_of(self.get_logout_button()))


    def get_setting_button(self):
        try:
            return self.driver.find_element_by_xpath('//div[i[@class="settings icon"]]')
        except:
            return None

    def get_logout_button(self):
        try:
            return self.driver.find_element_by_xpath('//span[text()="Log Out"]')
        except:
            return None