# Advent of Code
# Day 2
# Part 1

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
maxNumber = 14

#global variables
numberRegex = r"\d+"
result = 0

#get number - this returns the number from the line
def getNumber(x):
    x.split(' ',1)

#main function
def possibleGames():
    global result 
    #print('line', line)

    # find maximum number - if larger than 14 throw out line
    numbers = re.findall(numberRegex, line)
    numbers = np.array(numbers,dtype=int)
    #print('numbers',numbers)
    if (max(numbers) > maxNumber):
        print('number too large')
        return False
    else:
        print('valid game')
        return True

for index, line in enumerate(dataLines):
    realIndex = index + 1
    print('Game: :', realIndex)
    if possibleGames() == True:
        result += realIndex

print('final result: ',result)

