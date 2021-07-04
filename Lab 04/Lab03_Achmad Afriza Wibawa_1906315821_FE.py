# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 16:18:16 2019

@author: achmad.afriza
"""

# -----------------------------------beginning of program------------------------------------------------------------
print('Lab 03\n')
print('From decimal to binary')
print('----------------------')

# read the user's input
myInt = int(input('Give a positive integer in decimal representation: '))

# convert the integer stored in myInt to binary digits
binstr = '' # accumulator for binary digits, start with empty string
temp = myInt

while temp > 0:
 bindigit = str(temp%2)
 binstr = bindigit + binstr
 temp = temp//2
print('The binary representation of',myInt,'is','0b' + binstr)
print(
print('From binary to decimal')
print('----------------------')
# read the binary string from the user
binstr = input('Give a positive integer in binary representation: ')
# convert the binary string to a correct decimal integer
temp = binstr[2:] # remove '0b' using string slicing
newInt = 0 # accumulator for decimal value
length = len(temp)
for power in range(length):
 bindigitstr = temp[-1] # get the rightmost binary digit
 bindigit = int(bindigitstr)
 newInt = newInt + bindigit*2**power # add the appropriate power
 temp = temp[:-1] # remove the rightmost binary digit
print('The decimal representation of', binstr, 'is', newInt)
print()
print('Thanks for using this program.')
print()
input('Press Enter to continue ...') # hold the screen display

# -------------------------------------------end of program------------------------------------------------