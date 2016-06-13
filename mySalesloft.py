'''
Created on May 16, 2016

@author: seanbarow
'''
import time
from selenium import webdriver
from myHoovers import MyHoovers
from selenium.common.exceptions import WebDriverException
from mySiteObject import MySiteObject

class MySalesloft(MySiteObject):

    def __init__(self, tokenfile):
        '''
        Constructor
        '''
        #username, password = tokens
        MySiteObject.__init__(self, tokenfile)

        # Now open Salesloft
        self.browser = webdriver.Chrome('/users/seanbarow/pySean/chromedriver')
        self.browser.get('https://sdr.salesloft.com/app/dashboard')
        time.sleep(5)
        usernameElem = self.browser.find_element_by_id('user_email')
        usernameElem.send_keys(self.username)
        passwordElem = self.browser.find_element_by_id('user_password')
        passwordElem.send_keys(self.password)
        passwordElem.submit()
        print('Submitting username and password')
        time.sleep(5)
        
    def updateName(self, name, email):
        print(name)
        print(email)
        input('Click the correct person')
        time.sleep(5)
        # Click the edit button
        while True:
            try:
                edit_link = self.browser.find_element_by_class_name('contact-edit')
                edit_link.click()
                break;
            except WebDriverException:
                input('Is there anything in the way?')
        time.sleep(5)
        # Input the new email address
        emailText = self.browser.find_element_by_name('email1')
        print(self.browser.find_element_by_name('email1').text)
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
        html_list = self.browser.find_element_by_css_selector('div.information-tabs-heading')
        items = html_list.find_elements_by_tag_name("li")
        for item in items:
            if item.text == 'Cadences':
                item.click()
        viewInCRM = self.browser.find_element_by_css_selector('a.dropdown-toggle.ng-scope')
        viewInCRM.click()
        print('{}'.format(email))
        input('Set the email address and the cadence')
        
    def getBouncingEmails(self):
        # Click the People Element
        peopleElem = self.browser.find_element_by_css_selector('a.people')
        peopleElem.click()
        
        time.sleep(5)
        # Click on filter
        filterElem = self.browser.find_element_by_css_selector('span.btn.btn-default.btn--with-outline.dropdown-toggle')
        filterElem.click()
        
        input('Get the Bouncing emails and select all of them')
        
        # Click the People's action
        peopleActionElem = self.browser.find_element_by_css_selector('a.btn.btn-success.dropdown-toggle')
        peopleActionElem.click()
        
        # Click the Export button
        exportElem = self.browser.find_element_by_css_selector('a.ng-isolate-scope')
        exportElem.click()
        
        time.sleep(5)
        # Click the Yes confirm
        answerElem = self.browser.find_element_by_css_selector('a.btn.btn-confirm')
        answerElem.click()
