input = open('../data/p3_data.txt', 'r')

data = input.readlines()

curr_x = 0
curr_y = 0

x_width = 31
trees = 0
while curr_y < 322:
    curr_y += 1
    curr_x += 3
    if curr_x >= 31:
        curr_x = curr_x % 31
    pos = data[curr_y][curr_x]
    if pos == '#':
        trees += 1

print(trees)

