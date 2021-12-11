from collections import deque
from statistics import median
input = open('../data/p10_data.txt', 'r')
# input = open('../data/p10_test_data.txt', 'r')
lines = input.read().split('\n')
match_list = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}
points = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}


def calcuate_values(lines):
    line_totals = []
    for line in lines:
        line_total = 0
        stack = deque()
        fault = False
        for char in line:
            if char in ['[', '<', '(', '{']:
                stack.append(char)
            else:
                match = stack.pop()
                match_tuple = match_list[match]
                if match_tuple[0] != char:
                    fault = True
        if not fault:
            complete = []
            while len(stack) > 0:
                remain = stack.pop()
                complete.append(match_list[remain])
                line_total = (line_total * 5) + points[match_list[remain]]
            print('Line total: {}'.format(line_total))
            line_totals.append(line_total)

    return median(line_totals)


print("Score: {}".format(calcuate_values(lines)))
