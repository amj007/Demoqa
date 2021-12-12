from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://demoqa.com/books')

searchbox = driver.find_element_by_xpath('//*[@id="searchBox"]')
searchbox.send_keys('Git')

searchButton = driver.find_element_by_xpath('//*[@id="basic-addon2"]/span/svg')
searchButton.click()
