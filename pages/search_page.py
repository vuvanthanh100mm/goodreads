from locators.search_page_locators import SearchPageLocators
from commons.mobile_driver_handler import MobileDriverHandle
import time


class SearchPage:

    def __init__(self):

        self.search_page_locators = SearchPageLocators()
        self.driver_handler = MobileDriverHandle()

    def search_a_book(self, name_book):
        try:
            self.driver_handler.click_element(self.search_page_locators.search_box)
            self.driver_handler.send_keys(self.search_page_locators.search_text, name_book)
            self.driver_handler.click_element(self.search_page_locators.search_result)
            time.sleep(10)
        except Exception as e:
            raise Exception("Exception occured while search_a_book -->", e)

    def mark_a_reading(self):
        try:
            self.driver_handler.click_element(self.search_page_locators.search_box)
            time.sleep(10)
        except Exception as e:
            raise Exception("Exception occured while search_a_book -->", e)
