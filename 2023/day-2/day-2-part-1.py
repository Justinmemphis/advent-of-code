# Advent of Code
# Day 2
# Part 1

# thoughts:
# extract all red values from game - test against red in valid game conditions, etc.
# split line by , and ; (actually semi colons don't matter

import re
import numpy as np

#load input
#myfile = open('../input/day-2-input')
myfile = open('../input/day-2-test-1')
data = myfile.read()

dataLines = data.splitlines()

#valid game conditions
validGame = {
        "red": 12,
        "green": 13,
        "blue": 14
};
validMaxNumber = 14

#global variables
numberRegex = r"\d+"
result = 0

#get number - this returns the number from the line
def getNumber(phrase):
    return re.findall(numberRegex, phrase)[0]

def findColor(line):
    redMax = 0
    blueMax = 0
    greenMax = 0
    for x in line:
        if 'red' in x:
            y = int(getNumber(x))
            print('red number: ', y)
            if y > redMax:
                redMax = y
        elif 'blue' in x:
            y = int(getNumber(x))
            print('blue number: ', y)
            if y > blueMax:
                blueMax = y
        elif 'green' in x:
            y = int(getNumber(x))
            print('green number: ', y)
            if y > greenMax:
                greenMax = y
    print('redMax, blueMax, greenMax: ', redMax, blueMax, greenMax)

def stripColor(line):
    colors = re.split('[:,;]+',line)
    colors.pop(0) #remove the game line
    colors = [s.lstrip() for s in colors]
    print('colors: ', colors)
    print('findColor: ', findColor(colors))

#main function
def possibleGames(line):
    global result 
    #print('line', line)

    # find maximum number - if larger than 14 throw out line
    numbers = re.findall(numberRegex, line)
    numbers = np.array(numbers,dtype=int)
    #print('numbers',numbers)
    if (max(numbers) > validMaxNumber):
        print('number too large')
        return False
    else:
        print('valid game')
        stripColor(line)
        return True

for index, line in enumerate(dataLines):
    realIndex = index + 1
    print('Game: :', realIndex)
    if possibleGames(line) == True:
        result += realIndex

print('final result: ',result)

