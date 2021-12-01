input = open('../data/p9_test_data.txt', 'r')
preamble_len = 5

def check_for_sums(sum, window):
    for x in window:




xmas = input.read().splitlines()
xmas = [int(x) for x in xmas]
preamble = xmas[:preamble_len]
xmas = xmas[preamble:]

for x in xmas:
