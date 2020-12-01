from selenium import webdriver

class MainPage():
    def __init__(self, driver):
        self.driver = driver

        self.almaty_button = "btnFrom"
        self.where_button = "btnWhere"
        self.date_button = "btnDate"
        self.choose_date_button = "btnChoose"
        self.find_button = "btnFind"

    def click_from(self, from_btn):
        self.driver.find_element_by_xpath(self.from_button).click(from_btn)

    def click_where(self, where_btn):
        self.driver.find_element_by_xpath(self.where_button).click(where_btn)

    def click_date(self, date_btn):
        self.driver.find_element_by_xpath(self.date_button).click(date_btn)

    def choose_date(self, choose_btn):
        self.driver.find_element_by_xpath(self.choose_date_button).click(choose_btn)

    def click_find(self, find_btn):
        self.driver.find_element_by_xpath(self.find_button).click(find_btn)

