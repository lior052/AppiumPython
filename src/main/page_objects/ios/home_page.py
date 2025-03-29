import time

from appium.webdriver.common.appiumby import AppiumBy

from src.main.page_objects.ios.alert_view_page import AlertViewPage
from src.utils.ios.ios_actions import IOSAction


class HomePage(IOSAction):


    #ALERT_VIEWS_BTN = (AppiumBy.ACCESSIBILITY_ID, "Alert Views")

    def __init__(self, driver):
        super().__init__(driver)
        self.__alert_view_button = (AppiumBy.ACCESSIBILITY_ID, "Alert Views")
        self.__web_view_button = (AppiumBy.ACCESSIBILITY_ID, "Web View")

    def open_alert_view(self):
        self.driver.find_element(*self.__alert_view_button).click()

        return AlertViewPage(self.driver)
        #return self.alert_view_page

    def open_web_view(self):
        self.scroll_to_text_element("Web View")
        self.driver.find_element(*self.__web_view_button).click()

        #return AlertViewPage(self.driver)

    def back_to_home_page(self):
        self.driver.execute_script("mobile: terminateApp", {"bundleId": "com.example.apple-samplecode.UICatalog"})
        time.sleep(2)
        self.driver.execute_script("mobile: launchApp", {"bundleId": "com.example.apple-samplecode.UICatalog"})
