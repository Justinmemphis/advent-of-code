# Advent of Code
# Day 1
# Part 1

# test file
#print('Hello, World!')

# load input
# myfile = open('../input/day-1-test')
myfile = open('../input/day-1-input')
data = myfile.read()

# print first line of data
#print(data.split('\n', 1)[0])

dataLines = data.splitlines()

result = 0

for line in dataLines:
    first = 0
    last = 0
    sumLine = ''
    for i in line:
        #print('i',i)
        if i.isdigit():
            first = i
            break
    for j in reversed(line):
        #print('j',j)
        if j.isdigit():
            last = j
            break
    #print('Beginning Result is: ',result)
    sumLine = first + last
    #print('sumLine is: ',sumLine)
    result += int(sumLine)
    #print('Ending Result is: ',result)
    # print(line[0])

print(result)

