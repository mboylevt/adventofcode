# input = open('../data/p13_data.txt', 'r')
# ifile = '../data/p13_test_data.txt'
ifile = '../data/p13_data.txt'

from functools import cmp_to_key

def validate_order(left, right) -> int:
    if isinstance(left, int) and isinstance(right, int):
        if left == right:
            return 0
        if left < right:
            return 1
        if left > right:
            return -1
    elif isinstance(left, list) and isinstance(right, list):
        for idx in range(len(left)):
            if idx > len(right)-1:
                return -1
            result = validate_order(left[idx], right[idx])
            if result != 0:
                return result
        if len(right) > len(left):
            return 1
    elif isinstance(left, list) and isinstance(right, int):
        new_right = [right]
        result = validate_order(left, new_right)
        if result != 0:
            return result
    elif isinstance(left, int) and isinstance(right, list):
        new_left = [left]
        result = validate_order(new_left, right)
        if result != 0:
            return result
    return 0

pairs = [line for line in open(ifile, 'r').read().split('\n\n')]
per_line = [line for line in open(ifile, 'r').read().split('\n')]
pairs_p2 = []
for line in per_line:
    if line:
        pairs_p2.append(eval(line))
pairs_p2.append(eval('[[2]]'))
pairs_p2.append(eval('[[6]]'))

sum = 0
for idx, pair in enumerate(pairs):
    [left, right] = pair.split('\n')
    left = eval(left)
    right = eval(right)
    if validate_order(left, right) == 1:
       sum += idx + 1

print("Part 1: {}".format(sum))
s = sorted(pairs_p2, key=cmp_to_key(validate_order), reverse=True)
print("Part 2: {}".format((s.index([[2]]) + 1) * (s.index([[6]]) + 1)))