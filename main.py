from selenium import webdriver
from time import sleep
driver = webdriver.Chrome("./chromedriver")
driver.get("http://orteil.dashnet.org/cookieclicker/")
sleep(5)
while True: driver.find_element_by_id('bigCookie').click()
