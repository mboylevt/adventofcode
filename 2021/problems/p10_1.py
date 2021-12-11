from collections import deque
input = open('../data/p10_data.txt', 'r')
# input = open('../data/p10_test_data.txt', 'r')
lines = input.read().split('\n')
match_list = {
    '(': (')', 3),
    '[': (']', 57),
    '{': ('}', 1197),
    '<': ('>', 25137)
}
points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

total_points = 0
for line in lines:
    stack = deque()
    for char in line:
        if char in ['[', '<', '(', '{']:
            stack.append(char)
        else:
            match = stack.pop()
            fault = False
            match_tuple = match_list[match]
            if match_tuple[0] != char:
                print('Error - expected {} but got {}'.format(match_tuple[0], char))
                total_points += points[char]

print(total_points)
