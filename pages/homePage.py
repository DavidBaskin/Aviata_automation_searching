class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.from_xpath = "//body/div[6]/form[1]/div[1]/div[2]/div[1]/div[1]/span[2]/a[1]"
        self.to_xpath = "//body/div[6]/form[1]/div[1]/div[2]/div[1]/div[2]/span[2]/a[1]"
        self.from_date_xpath = "//body/div[6]/form[1]/div[1]/div[2]/div[2]/div[1]/img[1]"
        self.chose_date_xpath = "//a[normalize-space()='23']"
        self.button_search = "//button[contains(text(),'Найти билеты')]"

    def click_from(self):
        self.driver.find_element_by_xpath(self.from_xpath).click()


    def click_to(self):
        self.driver.find_element_by_xpath(self.to_xpath).click()

    def click_calendar(self):
        self.driver.find_element_by_xpath(self.from_date_xpath).click()

    def click_date(self):
        self.driver.find_element_by_xpath(self.chose_date_xpath).click()

    def click_search(self):
        self.driver.find_element_by_xpath(self.button_search).click()
