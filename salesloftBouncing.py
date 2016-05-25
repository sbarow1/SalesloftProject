'''
Created on Mar 14, 2016

@author: seanbarow
'''
import csv
import root.mySalesloft

tokenfile = 'tokens.txt'

# Read in csv file
bouncingNames = []
filename = input('What is the csv file?')
with open(filename, encoding='iso-8859-1') as bounceFile:
    bounceReader = csv.reader(bounceFile)
    headers = next(bounceReader)
    bouncingNames = [row[2] for row in bounceReader]

# Now open Salesloft
handler = root.mySalesloft.MySalesloft(tokenfile)

for name in bouncingNames:

    handler.updateName(name)
    
handler.closeBrowser()