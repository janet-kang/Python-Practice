# Created July 8, 2020
# This program asks for a username and password (password stays hidden from screen)
# and logs you into facebook.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import getpass

username = input('Username: ')
password = getpass.getpass()

url = 'https://www.facebook.com/'

driver = webdriver.Chrome('/Users/janetkang/Desktop/Programming/chromedriver')
driver.get(url)

driver.find_element_by_id('email').send_keys(username)
driver.find_element_by_id('pass').send_keys(password)
driver.find_element_by_id('loginbutton').click()