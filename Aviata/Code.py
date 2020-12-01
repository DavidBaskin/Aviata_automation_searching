driver.find_element_by_xpath("//body/div[6]/form[1]/div[1]/div[2]/div[1]/div[1]/input[2]").send_keys("Алматы")
driver.find_element_by_xpath("//body/div[6]/form[1]/div[1]/div[2]/div[1]/div[2]/input[2]").send_keys("Москва")
time.sleep(20)
import time

driver.get("https://aviata.kz")
driver.find_element_by_xpath("//body/div[6]/form[1]/div[1]/div[2]/div[1]/div[1]/span[2]/a[1]").click()
driver.find_element_by_xpath("//body/div[6]/form[1]/div[1]/div[2]/div[1]/div[2]/span[2]/a[1]").click()
driver.find_element_by_xpath("//body/div[6]/form[1]/div[1]/div[2]/div[2]/div[1]/img[1]").click()
driver.find_element_by_xpath("//body[1]/div[25]/div[1]/table[1]/tbody[1]/tr[5]/td[3]/a[1]").click()
driver.find_element_by_xpath("//button[contains(text(),'Найти билеты')]").click()
