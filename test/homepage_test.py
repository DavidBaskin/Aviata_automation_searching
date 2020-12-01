import allure
import moment
from selenium import webdriver

import pytest
from pages.homePage import HomePage
from utils import utils as utils


@pytest.mark.usefixtures("test_setup")
class TestLogin():

    def test_homepage(self):
        try:
            driver = self.driver
            driver.get(utils.URL)

            homepage = HomePage(driver)
            homepage.click_from()
            homepage.click_to()
            homepage.click_calendar()
            homepage.click_date()
            homepage.click_search()
            x = driver.title
            assert x == "Авиата - покупка авиабилетов онлай"

        except AssertionError as error:
            print("Assertion error occured")
            print(error)
            currTime = moment.now().strftime("%d-%m-%y_%H-%M-%S")
            testName = utils.whoami()
            screenshotName = testName+"_"+currTime
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            driver.get_screenshot_as_file("C:/Users/baski/aviata1/screenshots/" + screenshotName + ".png")
            raise

        except:
            print("There was an exception")

            currTime = moment.now().strftime("%d-%m-%y_%H-%M-%S")
            testName = utils.whoami()
            screenshotName = testName + "_" + currTime
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            driver.get_screenshot_as_file("C:/Users/baski/aviata1/screenshots" + screenshotName + ".png")
            raise

            print("No exception occured")
        finally:
            print("I`m an inside finally block")
