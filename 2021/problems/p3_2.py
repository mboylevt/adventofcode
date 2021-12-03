from copy import deepcopy

# input = open('../data/p3_test_data.txt', 'r')
input = open('../data/p3_data.txt', 'r')
lines = input.read().splitlines()
transpose = [list(row) for row in zip(*lines)]
length = len(lines[0])

oxygen = deepcopy(lines)
co2 = deepcopy(lines)
idx = 0

while True:
    o_transpose = [list(row) for row in zip(*oxygen)][idx]
    common = '1' if o_transpose.count('1') > o_transpose.count('0') else '0'
    if o_transpose.count('1') == o_transpose.count('0'):
        common = '1'
    new_oxygen = []
    for o_idx, entry in enumerate(oxygen):
        if entry[idx] == common:
            new_oxygen.append(oxygen[o_idx])
    oxygen = deepcopy(new_oxygen)
    if len(oxygen) == 1:
        break
    idx += 1

idx = 0
while True:
    c_transpose = [list(row) for row in zip(*co2)][idx]
    common = '1' if c_transpose.count('1') > c_transpose.count('0') else '0'
    if c_transpose.count('1') == c_transpose.count('0'):
        common = '1'
    new_co2 = []
    for c_idx, entry in enumerate(co2):
        if entry[idx] != common:
            new_co2.append(co2[c_idx])
    co2 = deepcopy(new_co2)
    if len(co2) == 1:
        break
    idx += 1

i = 1
co2rating = int(co2[0], 2)
o2rating = int(oxygen[0], 2)
print("Power consumption: {}".format(o2rating*co2rating))
