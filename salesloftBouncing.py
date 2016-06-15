'''
Created on Mar 14, 2016

@author: seanbarow
'''
import csv
import root.mySalesloft
import os

tokenfile = 'tokens.txt'

# Read in csv file
# Making bouncingNames a dictionary so that I can grab both
# the name and email, so I have the email address to print and
# keep track of later.
bouncingNames = {}
filename = input('What is the csv file?')
# Added this because I kept typing in the filename wrong.
while (os.path.isfile(filename) != True):
    filename = input('Nope try again, what is the csv file?')
with open(filename, encoding='iso-8859-1') as bounceFile:
    bounceReader = csv.reader(bounceFile)
    headers = next(bounceReader)
    bouncingNames = {row[2]: row[3] for row in bounceReader}

# Now open Salesloft
handler = root.mySalesloft.MySalesloft(tokenfile)

# If there is an unexpected error, make sure you close the browser.
try:
    for name, email in bouncingNames.items():
        handler.updateName(name, email)
finally:    
    handler.closeBrowser()
