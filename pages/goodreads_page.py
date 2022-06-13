from locators.goodreads_page_locators import GoodreadsPageLocators
from commons.mobile_driver_handler import MobileDriverHandle
import time


class GoodReadsPage:

    def __init__(self):

        self.goodreads_page_locators = GoodreadsPageLocators()
        self.driver_handler = MobileDriverHandle()

    def load_page(self):
        print('User is on "Goodreads" page')
        time.sleep(3)

    def click_login_lbl(self):
        try:
            self.driver_handler.click_element(self.goodreads_page_locators.login_lbl)
            time.sleep(3)
        except Exception as e:
            raise Exception("Exception occured while clicking on login button -->", e)
