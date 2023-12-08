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
    redMin = 0
    blueMin = 0
    greenMin = 0
    for x in line:
        if 'red' in x:
            y = int(getNumber(x))
            #print('red number: ', y)
            if y < redMin:
                redMin = y
        elif 'blue' in x:
            y = int(getNumber(x))
            #print('blue number: ', y)
            if y < blueMin:
                blueMin = y
        elif 'green' in x:
            y = int(getNumber(x))
            #print('green number: ', y)
            if y < greenMin:
                greenMin = y
    result += redMin * blueMin * greenMin

def stripColor(line):
    colors = re.split('[:,;]+',line)
    colors.pop(0) #remove the game line
    colors = [s.lstrip() for s in colors]
    print('colors: ', colors)
    findMin(colors)


for line in dataLines:
    global result
    stripColor(line)

print('final result: ',result)

