import os
import allure
from datetime import datetime

class AllureReport:

    @staticmethod
    def attach_screenshot(driver, name="screenshot"):
        """
        Captures a screenshot and attaches it to Allure report.
        """
        screenshot_path = f"reports/screenshots/{name}.png"
        driver.save_screenshot(screenshot_path)
        allure.attach.file(screenshot_path, name=name, attachment_type=allure.attachment_type.PNG)

