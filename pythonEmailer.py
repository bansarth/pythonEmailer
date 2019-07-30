from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def emailer():
    #load the web browser
    browser = webdriver.Firefox()
    browser.get('http://gmail.com')

    #get account info, recipient, subject, and message from the user.
    print('Please enter the gmail username for your account: ')
    username = input()
    print('Please enter the password for your account: ')
    password = input()
    print('Please enter the email address for the recipient of this email:')
    recipient = input()
    print('Please enter the subject line for this email:')
    subject = input()
    print('Please enter the message for this email:')
    messsage = input()

    #enter the email account
    emailElem = browser.find_element_by_id('identifierId')
    emailElem.send_keys(username)

    elem = browser.find_element_by_id('identifierNext')
    elem.click()
    time.sleep(5)

    emailElem = browser.find_element_by_name('password')
    emailElem.click()
    emailElem.send_keys(password)
    emailElem.send_keys(Keys.ENTER)


emailer()
