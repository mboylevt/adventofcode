input = open('../data/p3_data.txt', 'r')

data = input.readlines()

def tree_calc(x_slope, y_slope):
    curr_x = 0
    curr_y = 0

    x_width = 31
    trees = 0
    while curr_y < 322:
        curr_y += y_slope
        curr_x += x_slope
        if curr_x >= 31:
            curr_x = curr_x % 31
        pos = data[curr_y][curr_x]
        if pos == '#':
            trees += 1
    return trees


trees1 = tree_calc(1, 1)
trees3 = tree_calc(3, 1)
trees5 = tree_calc(5, 1)
trees7 = tree_calc(7, 1)
trees2 = tree_calc(1, 2)

print (trees7*trees5*trees3*trees2*trees1)


