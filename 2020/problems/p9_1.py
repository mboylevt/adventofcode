from copy import deepcopy

# input = open('../data/p9_test_data.txt', 'r')
# preamble_len = 5

input = open('../data/p9_data.txt', 'r')
preamble_len = 25


def check_for_sums(sum, window):
    for idx, x in enumerate(window):
        subwindow = deepcopy(window)
        subwindow.pop(idx)
        for y in subwindow:
            if x + y == sum:
                return True
    return False


xmas = input.read().splitlines()
xmas = [int(x) for x in xmas]
window = xmas[:preamble_len]
xmas = xmas[preamble_len:]

for x in xmas:
    if not check_for_sums(x, window):
        print(x)
        break
    window.pop(0)
    window.append(x)


