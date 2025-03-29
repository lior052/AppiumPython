import allure
import pytest
from src.tests.base.ios_base import IOSBaseTest
from src.utils.appium.appium_utils import AppiumUtils
from src.utils.allure_report import AllureReport


@pytest.mark.usefixtures("setup_class")
@allure.feature("Home Page")
@allure.story("Open Alert View")
@allure.severity(allure.severity_level.CRITICAL)
class TestHome(IOSBaseTest):


    def get_test_data(self):
        data = AppiumUtils.load_test_data()

    def test_home_open_alert_view(self):
        alert_page = self.home_page.open_alert_view()
        alert_page.tap_text_entry_menu()
        alert_page.fill_popup_text("PopUpText")
        alert_page.approve_popup()
        alert_page.tap_confirm_or_cancel_menu()
        confirm_message = alert_page.get_confirm_message_text()
        assert confirm_message == "A message should be a short, complete sentence."
        alert_page.confirm()

    def test_home_open_web_view(self):
        self.home_page.open_web_view()

    def test_dummy(self, test_data):
        popup_text = test_data.get("popup_text")

        alert_page = self.home_page.open_alert_view()
        alert_page.tap_text_entry_menu()
        alert_page.fill_popup_text(popup_text)