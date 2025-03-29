import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options


class AndroidBaseTest:
    driver = None

    @pytest.fixture(scope="class", autouse=True)
    def setup_class(self, request):

        options = UiAutomator2Options()
        options.platform_name = "Android"
        options.device_name = "pixel 8 pro"
        options.app = "/Users/lior/PycharmProjects/AppiumPythonFramework/src/tests/apps/General-Store.apk"
        options.automation_name = "UIAutomator2"
        options.set_capability("uiautomator2ServerLaunchTimeout", 60000)

        AndroidBaseTest.driver = webdriver.Remote("http://localhost:4723", options=options)

        request.cls.driver = AndroidBaseTest.driver
        AndroidBaseTest.driver.implicitly_wait(10)

        yield
        AndroidBaseTest.driver.quit()