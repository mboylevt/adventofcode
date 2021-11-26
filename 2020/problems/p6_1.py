import math

input = open('../data/p6_data.txt', 'r')

raw_input = input.read()
groups = raw_input.split('\n\n')

sum = 0
for group in groups:
    group = sorted(group.replace('\n', ''))
    #print(group)
    #print(sorted(set(group)))
    sum += len(set(group))

print(sum)