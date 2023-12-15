# Advent of Code
# Day 2
# Part 2

# thoughts:
# just find max numbers and then multiple redMax * blueMax * greenMax and add to result
#

import re

#load input
myfile = open('../input/day-2-input')
#yfile = open('../input/day-2-test-1')
data = myfile.read()

dataLines = data.splitlines()

#global variables
numberRegex = r"\d+"
result = 0

#get number - this returns the number from the line
def getNumber(phrase):
    return re.findall(numberRegex, phrase)[0]

def findMax(line):
    colors = re.split('[:,;]+',line)
    colors.pop(0) #remove the game line
    colors = [s.lstrip() for s in colors]
    print('colors: ', colors)

    redMax = None
    blueMax = None
    greenMax = None
    for x in colors:
        print('this is x: ',x)
        if 'red' in x:
            y = int(getNumber(x))
            if redMax == None:
                redMax = y
            elif y > redMax:
                redMax = y
        elif 'blue' in x:
            y = int(getNumber(x))
            if blueMax == None:
                blueMax = y
            elif y > blueMax:
                blueMax = y
        elif 'green' in x:
            y = int(getNumber(x))
            if greenMax == None:
                greenMax = y
            elif y > greenMax:
                greenMax = y
        
    '''
    for x in line:
        print('this is x: ',x)
        '''
    '''
    for x in line:
                '''
    print('redMax, blueMax, greenMax',redMax,blueMax, greenMax)
    if redMax == None:
        redMax = 1
    if blueMax == None:
        blueMax = 1
    if greenMax == None:
        greenMax = 1
    return redMax * blueMax * greenMax

for line in dataLines:
    product = findMax(line)
    result += product

print('final result: ',result)

