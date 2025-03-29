import pytest
import logging
import os
import allure
from datetime import datetime
from src.utils.appium.appium_utils import AppiumUtils
from src.utils.allure_report import AllureReport


@pytest.fixture(scope="session", autouse=True)
def setup_logging():
    """Set up global logging for test execution."""
    log_dir = "reports/logs"
    os.makedirs(log_dir, exist_ok=True)

    log_file = os.path.join(log_dir, f"test_run_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log")
    logging.basicConfig(filename=log_file, level=logging.INFO,
                        format="%(asctime)s - %(levelname)s - %(message)s",
                        datefmt="%Y-%m-%d %H:%M:%S")
    logging.info("Test session started.")

@pytest.fixture(scope="session")
def test_data():
    """Load test data once per test session."""
    return AppiumUtils.load_test_data()  # Ensures test data is accessible in all tests

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    """Capture screenshots and attach to Allure on test failure."""
    outcome = yield
    report = outcome.get_result()

    # Store test report for later use in fixtures
    setattr(item, "test_result", report)

    if report.when == "call" and report.failed:  # Only attach on actual test failure
        driver = getattr(item.cls, "driver", None)
        if driver:
            AllureReport.attach_screenshot(driver, name=item.name)

@pytest.fixture(scope="function", autouse=True)
def log_test_status(request):
    """Log test start and result status."""
    test_name = request.node.name
    logging.info(f"Running test: {test_name}")

    yield  # Run the test

    # Retrieve test result from `pytest_runtest_makereport`
    report = getattr(request.node, "test_result", None)

    if report and report.failed:
        logging.error(f"Test failed: {test_name}")
    else:
        logging.info(f"Test passed: {test_name}")
