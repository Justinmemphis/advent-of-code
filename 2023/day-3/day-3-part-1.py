'''
Advent of Code
Day 3
Part 1
2023
'''

'''
Strategy:

    function - check for symbol around index

    iterate over the line left to right
        if it is a digit
            check if symbol in neighboring 7
                if symbol store char in temp
            if space to right
                check seven around that digit
                    add to temp

    iterate over the line
        grab digits by regex split by delimiters


    push whole input into a matrix array
        per character
    grab digits lumped together (numbers)
        with their starting and ending positions
    if any of the following meet symbol regex
        add whole number to result:
            row before same position
            row after same position
            same row before
            same row after
            row before beg -1 and end +1
            row after beg -1 and end +1
    return result

    discrete functions:
        symbol regex
        global variable result
        function to sum part numbers / find
            digit length
                (need temp variable here to
                count length of number and
                beginning/end position)

    note - numpy has diagonal if needed

'''
import re
import numpy as np
#from io import BytesIO

# load input
#myfile = open('../input/day-3-input')
myfile = open('../input/day-3-test-1')
data = myfile.read()
symbolRegex = r"\.|\*|\#|\+|\$|\/|\=|\&|\@|\!|\^"

#print(type(data)) == string
lines = data.split('\n')
print('lines: ',lines)

#pad lines - only needed for last, blank line
wid = max(len(w) for w in lines)
arr = np.array([ list(w.center(wid)) for w in lines])

#remove last unnecessary line
arr = arr[:-1, :]


print('arr:')
print(arr)
print(type(arr))
print(arr.shape)
print(arr.dtype)
#y_size, x_size = arr.shape
#print('y_size: ',y_size)
#print('x_size: ',x_size)


'''
arr = [row for row in data.split('\n')]
def checkForSymbol(x):
    if 

for line in arr:
    # get numbers
    numbers = re.split(symbolRegex,line)

    # remove empty strings
    numbers = [x for x in numbers if x]

    print('numbers',numbers)

#a = np.loadtxt(data)
#a = np.genfromtxt(BytesIO(data.encode('utf-8')), dtype=np.int64)

print('arr: ',arr)

#print('a[2,2]: ',a[2,2])
'''
