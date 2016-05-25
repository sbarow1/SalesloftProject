'''
Created on May 16, 2016

@author: seanbarow
'''
import root.mySalesloft

handler = root.mySalesloft.MySalesloft('tokens.txt')

handler.getBouncingEmails()

handler.closeBrowser()
