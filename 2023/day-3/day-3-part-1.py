'''
Advent of Code
Day 3
Part 1
2023
'''

'''
Strategy:
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
import numpy as np
from io import BytesIO

# load input
#myfile = open('../input/day-3-input')
myfile = open('../input/day-3-test-1')
data = myfile.read()

a = [row for row in data.split('\n')]
#a = np.loadtxt(data)
#a = np.genfromtxt(BytesIO(data.encode('utf-8')), dtype=np.int64)
print('a: ',a)
#print('a[2,2]: ',a[2,2])
