# Advent of Code
# Day 2
# Part 1

import re

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

#get number
def getNumber(x):
    x.split(' ',1)

#main function
def possibleGames():
    global result 
    print('line', line)

    # find maximum number - if larger than 14 throw out line
    numbers = re.findall(numberRegex, line)
    print('numbers',numbers)
    #convert to int
    for x in numbers:
        int(x)
    if (int(max(numbers)) > maxNumber):
        print('number too large')
        return
    

for line in dataLines:
    possibleGames()

print('final result: ',result)

