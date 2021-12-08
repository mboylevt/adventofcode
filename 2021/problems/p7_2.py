input = open('../data/p7_data.txt', 'r')
# input = open('../data/p7_test_data.txt', 'r')
crabs = input.read().split(',')
crabs = [int(x) for x in crabs]


def sigma(start, end):
    sum = 0
    new_end = end - start + 1
    for x in range(1, new_end):
        sum += x
    return sum


minpos = min(crabs)
maxpos = max(crabs)
position_weights = {}
for pos in range(minpos, maxpos+1):
    total_fuel = 0
    for crab in crabs:
        fuel = 0 # this doesn't change if they're equivalent, so no need to test
        if crab > pos:
            fuel = sigma(pos, crab)
        elif crab < pos:
            fuel = sigma(crab, pos)
        total_fuel += fuel
    position_weights[pos] = total_fuel

bestpos = min(position_weights, key=position_weights.get)
print('pos {}: Fuel {}'.format(bestpos, position_weights[bestpos]))
i = 1