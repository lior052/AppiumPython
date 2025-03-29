import pytest
from appium import webdriver
from appium.options.ios import XCUITestOptions
from appium.webdriver.appium_service import AppiumService

from src.main.page_objects.ios.home_page import HomePage
from src.utils.appium.appium_utils import AppiumUtils


class IOSBaseTest:
    driver = None
    home_page = None

    @pytest.fixture(scope="class", autouse=True)
    def setup_class(self, request):

        appium_service = AppiumService()
        appium_service.start()

        device_caps = AppiumUtils.load_ios_device_config()  # Fetch iOS device data
        options = XCUITestOptions().load_capabilities(device_caps) # Convert YAML dictionary to XCUITestOptions

        # options = XCUITestOptions()
        # options.platform_name = "iOS"
        # options.device_name = "iPhone 13 Pro"
        # options.platform_version = "18.3"
        # options.app = "/Users/lior/Library/Developer/Xcode/DerivedData/UIKitCatalog-ffbfzacbhfcgzecvsxrzacugnuyv/Build/Products/Debug-iphonesimulator/UIKitCatalog.app"
        # options.automation_name = "XCUITest"

        IOSBaseTest.driver = webdriver.Remote("http://localhost:4723", options=options)
        IOSBaseTest.driver.implicitly_wait(10)

        # init the home page
        IOSBaseTest.home_page = HomePage(self.driver)

        request.cls.driver = IOSBaseTest.driver
        request.cls.home_page = IOSBaseTest.home_page

        yield
        self.driver.execute_script("mobile: terminateApp", {"bundleId": "com.example.apple-samplecode.UICatalog"})
        IOSBaseTest.driver.quit()
        appium_service.stop()

    @pytest.fixture(scope="function", autouse=True)
    def teardown_driver(self):
        yield
        IOSBaseTest.home_page.back_to_home_page()
