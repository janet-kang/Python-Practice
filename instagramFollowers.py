# create July 8, 2020

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import getpass


# get username and password from user
username = input('Username: ')
password = getpass.getpass()

# open instagram in browser
url = 'https://www.instagram.com/'

driver = webdriver.Chrome('/Users/janetkang/Desktop/Programming/chromedriver')
driver.get(url)

# log in to Instagram
sleep(2) # needs to wait or instagram thinks its a bot?

inputUser = driver.find_element_by_xpath('//input[@name="username"]') # finds username box
inputPass = driver.find_element_by_xpath('//input[@name="password"]') # finds password box

inputUser.send_keys(username) # enter username
inputPass.send_keys(password) # enter password
inputPass.send_keys(Keys.RETURN) # press ENTER to log in

# navigate to profile
sleep(5)
driver.get(url + username + '/followers/')

# navigate to followers
#sleep(5)
#followersButton = driver.find_element_by_name(' _81NM2')
#followersButton.click()
#driver.get(url + username + '/followers/')

