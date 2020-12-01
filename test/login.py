import time

from selenium import webdriver

import pytest


class TestLogin():
    @pytest.fixture(scope="class")
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(executable_path="C:/Users\/baski/aviata1/drivers/chromedriver.exe")
        driver.implicitly_wait(5)
        driver.maximize_window()
        yield
        time.sleep(15)
        driver.back()
        time.sleep(5)
        driver.close()
        driver.quit()
        print("Test completed")

    def test_main(self, test_setup):
        driver.get("https://aviata.kz/")
        driver.find_element_by_xpath("//body/div[6]/form[1]/div[1]/div[2]/div[1]/div[1]/span[2]/a[1]").click()
        driver.find_element_by_xpath("//body/div[6]/form[1]/div[1]/div[2]/div[1]/div[2]/span[2]/a[1]").click()
        driver.find_element_by_xpath("//body/div[6]/form[1]/div[1]/div[2]/div[2]/div[1]/img[1]").click()
        driver.find_element_by_xpath().click()
        driver.find_element_by_xpath("//button[contains(text(),'Найти билеты')]").click()
