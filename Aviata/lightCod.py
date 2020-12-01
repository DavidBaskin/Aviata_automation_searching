import time

from selenium import webdriver

driver = webdriver.Chrome("C:/Users/baski/aviata1/drivers/chromedriver.exe")

driver.implicitly_wait(5)

driver.maximize_window()

driver.get("https://aviata.kz")
driver.find_element_by_xpath("//body/div[6]/form[1]/div[1]/div[2]/div[1]/div[1]/span[2]/a[1]").click()
driver.find_element_by_xpath("//body/div[6]/form[1]/div[1]/div[2]/div[1]/div[2]/span[2]/a[1]").click()
driver.find_element_by_xpath("//body/div[6]/form[1]/div[1]/div[2]/div[2]/div[1]/img[1]").click()
driver.find_element_by_xpath("//body[1]/div[25]/div[1]/table[1]/tbody[1]/tr[5]/td[3]/a[1]").click()
driver.find_element_by_xpath("//button[contains(text(),'Найти билеты')]").click()


time.sleep(10)
driver.close()
driver.quit()
