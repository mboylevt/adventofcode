import sys

input = open('../data/p13_data.txt', 'r')

data = input.readlines()
buses = list(data[1].strip().split(','))
buses = [(int(buses[i]), (int(buses[i]) - i) % int(buses[i]))
    for i in range(len(buses)) if buses[i] != 'x']

result = 0
increment = 1

for bus in buses:
    while result % bus[0] != bus[1]:
        result += increment
    increment *= bus[0]

print(result)