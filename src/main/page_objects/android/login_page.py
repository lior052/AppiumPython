from appium.webdriver.common.appiumby import AppiumBy

class LoginPage:

    APPLY_BTN = (AppiumBy.ID, "btnLetsShop")
    COUNTRY_BOX = (AppiumBy.ID, "spinnerCountry")
    MALE_OPTION = (AppiumBy.XPATH, "//android.widget.RadioButton[@text='Male']")
    FEMALE_OPTION = (AppiumBy.XPATH, "//android.widget.RadioButton[@text='Female']")
    NAME_TEXT_BOX = (AppiumBy.ID, "nameField")

    def __init__(self, driver):
        self.driver = driver #self.__alert_view_button = (AppiumBy.ACCESSIBILITY_ID, "Alert Views")

    def set_name_text(self, name):
        self.driver.find_element(*self.NAME_TEXT_BOX).send_keys(name)
        self.driver.hide_keyboard()
