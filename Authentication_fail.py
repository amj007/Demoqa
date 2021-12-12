from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://demoqa.com/login')

username = 'testuser'
password = 'testpass'

user_input = driver.find_element_by_id('userName')
user_input.send_keys(username)


pass_input = driver.find_element_by_id('password')
pass_input.send_keys(password)

login_button = driver.find_element_by_id('login')
login_button.click()

time.sleep(2)

if(driver.find_element_by_id('name').is_displayed()):
    print("Login failed")
else:
    print("login success")