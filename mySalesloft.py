'''
Created on May 16, 2016

@author: seanbarow
'''
import time
from selenium import webdriver
from myHoovers import MyHoovers

class MySalesloft():
    '''
    classdocs
    '''


    def __init__(self, tokenfile):
        '''
        Constructor
        '''
        # Get username and password
        with open(tokenfile, 'r') as f:
            tokens = f.read().split()
    
        username, password = tokens

        # Now open Salesloft
        driver = webdriver.Chrome('/users/seanbarow/pySean/chromedriver')
        self.driver = driver
        driver.get('https://sdr.salesloft.com/app/dashboard')
        time.sleep(5)
        usernameElem = driver.find_element_by_id('user_email')
        usernameElem.send_keys(username)
        passwordElem = driver.find_element_by_id('user_password')
        passwordElem.send_keys(password)
        passwordElem.submit()
        print('Submitting username and password')
        time.sleep(5)
        
    def updateName(self, name):
        print(name)
        input('Click the correct person')
        time.sleep(5)
        # Click the edit button
        edit_link = self.driver.find_element_by_class_name('contact-edit')
        edit_link.click()
        time.sleep(5)
        # Input the new email address
        emailText = self.driver.find_element_by_name('email1')
        print(self.driver.find_element_by_name('email1').text)
        emailText.clear()
    
        # Open a Hoover's instance to find the correct email address
        handlerH = MyHoovers()
    # Search Hoovers
        handlerH.hooverSearch(name)
        input('Are you done?')
        handlerH.closeBrowser()
        #driverH.close()
        email = input('What is the correct email address?')
        emailText.send_keys(email)
        emailText.submit()
        time.sleep(5)
        html_list = self.driver.find_element_by_css_selector('div.information-tabs-heading')
        items = html_list.find_elements_by_tag_name("li")
        for item in items:
            if item.text == 'Cadences':
                item.click()
        viewInCRM = self.driver.find_element_by_css_selector('a.dropdown-toggle.ng-scope')
        viewInCRM.click()
        print('{}'.format(email))
        input('Set the email address and the cadence')
        
    def getBouncingEmails(self):
        # Click the People Element
        peopleElem = self.driver.find_element_by_css_selector('a.people')
        peopleElem.click()
        
        time.sleep(5)
        # Click on filter
        filterElem = self.driver.find_element_by_css_selector('span.btn.btn-default.btn--with-outline.dropdown-toggle')
        filterElem.click()
        
        input('Get the Bouncing emails and select all of them')
        
        # Click the People's action
        peopleActionElem = self.driver.find_element_by_css_selector('a.btn.btn-success.dropdown-toggle')
        peopleActionElem.click()
        
        # Click the Export button
        exportElem = self.driver.find_element_by_css_selector('a.ng-isolate-scope')
        exportElem.click()
        
        time.sleep(5)
        # Click the Yes confirm
        answerElem = self.driver.find_element_by_css_selector('a.btn.btn-confirm')
        answerElem.click()
        
    def closeBrowser(self):
        self.driver.close()
        print('See Ya!')