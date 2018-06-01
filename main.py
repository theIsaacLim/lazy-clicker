from selenium import webdriver
driver = webdriver.Chrome("./chromedriver")
driver.get("http://orteil.dashnet.org/cookieclicker/")
driver.implicitly_wait(5)
c = driver.find_element_by_id('bigCookie')
while True: c.click()
