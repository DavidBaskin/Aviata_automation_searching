
import pytest
import time


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Type in browser name e.g. chrome OR firefox")


@pytest.fixture(scope="class")
def test_setup(request):
    from selenium import webdriver

    browser = request.config.getoption("--browser")

    if browser == 'chrome':
        driver = webdriver.Chrome(
            executable_path="C:/Users/baski/aviata1/drivers/chromedriver.exe")
    elif browser == 'firefox':
        driver = webdriver.Firefox(
            executable_path="C:/Users/baski/aviata1/drivers/geckodriver.exe")

    driver.implicitly_wait(5)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    time.sleep(10)
    driver.back()
    time.sleep(2)
    driver.close()
    driver.quit()
    print("Test completed")
