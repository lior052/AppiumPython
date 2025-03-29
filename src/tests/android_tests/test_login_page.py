import pytest
from src.main.page_objects.android.login_page import LoginPage
from src.tests.base.android_base import AndroidBaseTest


@pytest.mark.usefixtures("setup_class")
class TestHome(AndroidBaseTest):


    def test_login(self):
        login_page = LoginPage(self.driver)
        login_page.set_name_text("Lio")

        #assert "Dashboard" in self.driver.page_source  # Dummy assertion
