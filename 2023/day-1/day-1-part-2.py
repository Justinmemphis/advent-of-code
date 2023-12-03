# Advent of Code
# Day 1
# Part 2

# HOW TO SOLVE - CHANGE WORD SOLUTION - JUST LOOK AT LETTERS - FIRST WORD, LAST WORD - DON'T HANDLE EDGE CASES (TOO MANY)

import regex as re

# load input
#myfile = open('../input/day-1-test-2')
myfile = open('../input/day-1-input')
#myfile = open('../input/day-1-test-3')
data = myfile.read()

dataLines = data.splitlines()

numbers = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine"
]

regex = r"(\d|one|two|three|four|five|six|seven|eight|nine)"

result = 0

def calibrate():
    global result
    print('line',line)

    digits = re.findall(regex, line, overlapped=True)
    first = digits[0]
    last = digits[-1]

    if len(first) > 1:
        first = numbers.index(first) + 1

    if len(last) > 1:
        last = numbers.index(last) + 1

    sumLines = f"{first}{last}"
    result += int(sumLines)

    """
    firstDigitIndex = 9999999
    lastDigitIndex = -9999999
    firstWordIndex = 999999
    lastDigitIndex = -999999
    firstDigit = 0
    lastDigit = 0
    firstWord = ''
    lastWord = ''

    # find first digit
    for index, i in enumerate(line):
        #print('i',i)
        if i.isdigit():
            firstDigit = i
            firstDigitIndex = index
            break

    # find last digit
    for index, j in enumerate(line):
        #print('j',j)
        if j.isdigit():
            lastDigit = j
            lastDigitIndex = index

    resultArr = [firstDigit, firstDigitIndex, lastDigit, lastDigitIndex]
    #print('digit1, index, digit2, index: ',resultArr)

    # find first word
    for match in re.finditer(regex, line):
        firstWord = match.group()
        firstWordIndex = match.start()
        #print(match.span(), match.group())
        #print('firstWord, firstWordIndex :',firstWord,firstWordIndex)
        break

    # find last word
    for match in re.finditer(regex, line, overlapped=True):
        lastWord = match.group()
        lastWordIndex = match.end()
        #print(match.span(), match.group())
        #print('lastWord, lastWordIndex :',lastWord,lastWordIndex)
    
    #print('firstWord, firstWordIndex, lastWord, lastWordIndex :',firstWord, firstWordIndex, lastWord, lastWordIndex)

    wordDict = {
        'one': 1,
        'ne': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'ight': 8,
        'nine': 9
    }

    #print('one',wordDict.get('one'))

    if (firstWord or lastWord):

        # test if first word comes before first digit and replace value if true
        if firstWordIndex < firstDigitIndex:
            resultArr[0] = wordDict.get(firstWord)

        # test if last word comes after last digit and replace value if true
        if lastWordIndex > lastDigitIndex:
            resultArr[2] = wordDict.get(lastWord)

    if resultArr[0] and resultArr[2]:
        sumLine = str(resultArr[0]) + str(resultArr[2])
    elif resultArr[0]:
        sumLine = str(resultArr[0])
    elif resultArr[1]:
        sumline = str(resultArr[2])
    else:
        print('no number')

    print('number for line: ',sumLine)
    result += int(sumLine)
    """

    #print('end of line result: ',result)

for line in dataLines:
    calibrate()

print('final result: ',result)


