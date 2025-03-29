from appium.webdriver.common.appiumby import AppiumBy

class AlertViewPage:

    TXT_FIELD_POPUP = (AppiumBy.CLASS_NAME, "XCUIElementTypeTextField")
    OK_BTN = (AppiumBy.ACCESSIBILITY_ID, "OK")

    def __init__(self, driver):
        self.driver = driver
        self.__txt_entry_menu_button = (AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeStaticText[`name == 'Text Entry'`]")
        self.__confirm_cancel_menu_button = (AppiumBy.IOS_PREDICATE, "name BEGINSWITH 'Confirm' AND type == 'XCUIElementTypeStaticText'")
        self.__txt_field_popup = (AppiumBy.CLASS_NAME, "XCUIElementTypeTextField")
        self.__ok_button = (AppiumBy.ACCESSIBILITY_ID, "OK")
        self.__confirm_message = (AppiumBy.IOS_PREDICATE, "name BEGINSWITH 'A message'")
        self.__confirm_button = (AppiumBy.ACCESSIBILITY_ID, "Confirm")



    def tap_text_entry_menu(self):
        self.driver.find_element(*self.__txt_entry_menu_button).click()

    def fill_popup_text(self, text):
        self.driver.find_element(*self.__txt_field_popup).send_keys(text)

    def approve_popup(self):
        self.driver.find_element(*self.__ok_button).click()

    def confirm(self):
        self.driver.find_element(*self.__confirm_button).click()

    def tap_confirm_or_cancel_menu(self):
        self.driver.find_element(*self.__confirm_cancel_menu_button).click()

    def get_confirm_message_text(self):
        return self.driver.find_element(*self.__confirm_message).text
