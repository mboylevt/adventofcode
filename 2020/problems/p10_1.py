from copy import deepcopy


input = open('../data/p10_data.txt', 'r')
# input = open('../data/p10_test_data.txt', 'r')

adaptors = input.read().splitlines()
adaptors =sorted([int(x) for x in adaptors])

# for adaptor in adaptors:
#
# starting_jolts = 0
# adaptors_in_order = []
diffs = {1:0, 2:0, 3:0}
for index, adaptor in enumerate(adaptors):
    if index == len(adaptors)-1:
        diffs[3]+= 1
        break
    if index == 0:
        diffs[adaptor] += 1
    diff = adaptors[index+1] - adaptor
    diffs[diff] += 1
print(diffs)
print(diffs[1] * diffs[3])


