# Advent of Code
# Day 2
# Part 2

# thoughts:
# just find min numbers and then multiple redMin * blueMin * greenMin and add to result

import re

#load input
#myfile = open('../input/day-2-input')
myfile = open('../input/day-2-test-1')
data = myfile.read()

dataLines = data.splitlines()

#global variables
numberRegex = r"\d+"
result = 0

#get number - this returns the number from the line
def getNumber(phrase):
    return re.findall(numberRegex, phrase)[0]

def findMin(line):
    colors = re.split('[:,;]+',line)
    colors.pop(0) #remove the game line
    colors = [s.lstrip() for s in colors]
    print('colors: ', colors)

    redMin = None
    blueMin = None
    greenMin = None
    for x in line:
        if 'red' in x:
            y = int(getNumber(x))
            if y < redMin:
                redMin = y
        elif 'blue' in x:
            y = int(getNumber(x))
            if y < blueMin:
                blueMin = y
        elif 'green' in x:
            y = int(getNumber(x))
            if y < greenMin:
                greenMin = y
    print('redMin, blueMin, greenMin',redMin,blueMin, greenMin)
    if redMin == None:
        redMin = 1
    if blueMin == None:
        blueMin = 1
    if greenMin == None:
        greenMin = 1
    return redMin * blueMin * greenMin

for line in dataLines:
    product = findMin(line)
    result += product

print('final result: ',result)

