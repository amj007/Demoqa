from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("https://demoqa.com/automation-practice-form")

First_Name = driver.find_element_by_xpath('//*[@id="firstName"]').send_keys('testfirstname')

last_Name = driver.find_element_by_xpath('//*[@id="lastName"]').send_keys('testlastname')

Email = driver.find_element_by_xpath('//*[@id="userEmail"]').send_keys('testlastname_test@test.com')

Mobile = driver.find_element_by_xpath('//*[@id="userNumber"]').send_keys('01234567890')

female = driver.find_element_by_id("genterWrapper").click()

dob = driver.find_element_by_id('dateOfBirthInput').click()

dob = driver.find_element_by_xpath('//*[@id="dateOfBirth"]/div[2]/div[2]/div/div/div[2]/div[2]/div[3]/div[4]').click()

#subject = driver.find_element_by_class('css-2b097c-container').click().send_keys('h')

currentaddress = driver.find_element_by_id('currentAddress').send_keys('Slough, UK')

#hobbies = driver.find_element_by_id("hobbies-checkbox-2").click()


submit = driver.find_element_by_xpath('//*[@id="submit"]').click()

