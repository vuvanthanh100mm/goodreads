from appium.webdriver.common.mobileby import MobileBy as mobily_by
from appium import webdriver


class MobileDriverHandle():

    def __init__(self):
        sauce_url = "http://127.0.0.1:4723/wd/hub"
        desired_caps = {
            'autoGrantPermissions': True,
            'platformName': 'Android',
            'platformVersion': '11',
            'deviceName': 'R9YRA0QGAXN',
            'deviceOrientation': 'portrait',
            'app': 'C:\\Users\\vuvan\\PycharmProjects\\PytestBDD_framework\\Yield\\Appium\\goodreads\\source\\Goodreads.apk',
            'appPackage': 'com.goodreads',
            'appWaitActivity': 'com.goodreads.kindle.ui.activity.LandingActivity',
            'full-reset': True
        }
        self.driver = webdriver.Remote(sauce_url, desired_caps)

    def get_driver(self):
        return self.driver

    def get_by(self, locator_type):
        try:
            if locator_type.lower() == 'xpath':
                locator_by = mobily_by.XPATH
            elif locator_type.lower() == 'id':
                locator_by = mobily_by.ID
            elif locator_type.lower() == 'css':
                locator_by = mobily_by.CSS_SELECTOR
            elif locator_type.lower() == 'link':
                locator_by = mobily_by.LINK_TEXT
            else:
                raise Exception("By of Locator not found for -->", locator_type)
            return locator_by
        except Exception as e:
            raise Exception("Error occurred while getting the by -->", e)

    def get_element(self, locator):
        try:
            split_locator = locator.split('~')
            locator_by = self.get_by(split_locator[0])
            locator_path = split_locator[1]
            ele = self.get_driver().find_element(by=locator_by, value=locator_path)
            return ele
        except Exception as e:
            raise Exception("Error occurred while getting the element:", e)

    def click_element(self, locator):
        try:
            self.get_element(locator).click()
        except Exception as e:
            raise Exception("Exception occurred while clicking element:", e)

    def send_keys(self, locator, text):
        try:
            self.get_element(locator).send_keys(text)
        except Exception as e:
            raise Exception("Exception occurred while sending text to element:", locator, "-->", e)
