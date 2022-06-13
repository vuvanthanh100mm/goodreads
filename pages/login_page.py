from locators.login_page_locators import LoginPageLocators
from commons.mobile_driver_handler import MobileDriverHandle
import time


class LoginPage:

    def __init__(self):

        self.login_page_locators = LoginPageLocators()
        self.driver_handler = MobileDriverHandle()

    def enter_username(self, username):
        try:
            self.driver_handler.send_keys(self.login_page_locators.username_input, username)
        except Exception as e:
            raise Exception("Exception occured while entering username -->", e)

    def enter_password(self, password):
        try:
            self.driver_handler.send_keys(self.login_page_locators.password_input, password)
        except Exception as e:
            raise Exception("Exception occured while entering password -->", e)

    def click_login_btn(self):
        try:
            self.driver_handler.click_element(self.login_page_locators.login_btn)
            time.sleep(10)
        except Exception as e:
            raise Exception("Exception occured while clicking on login button -->", e)
