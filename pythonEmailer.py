from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
import sys

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
    message = input()

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

    time.sleep(10)
    builder = ActionChains(browser)
    builder.send_keys('c')
    builder.perform()
    time.sleep(2)

    recip = ActionChains(browser)
    recip.send_keys(recipient)
    recip.perform()
    tabs =  ActionChains(browser)
    tabs.send_keys(Keys.TAB)
    tabs.perform()
    tabs.perform()
    sched = ActionChains(browser)
    sched.send_keys(subject)
    sched.perform()
    tabs.perform()
    mess = ActionChains(browser)
    mess.send_keys(message)
    mess.perform()
    tabs.perform()
    enter = ActionChains(browser)
    enter.send_keys(Keys.ENTER)
    enter.perform()
    
emailer()
