# input = open('../data/p14_data.txt', 'r')
# ifile = '../data/p14_test_data.txt'
ifile = '../data/p14_data.txt'

def get_segment_coords(segment):
    x = int(segment.split(',')[0])
    y = int(segment.split(',')[1])
    return [x,y]

def draw_rocks(cave, rocks, min_x):
    for rock in rocks:
        segments = rock.split(' -> ')
        for idx in range(len(segments)-1):
            [start_x, start_y] = get_segment_coords(segments[idx])
            [end_x, end_y] = get_segment_coords(segments[idx+1])
            if start_x == end_x:  # we're going down
                if start_y < end_y:
                    for y in range(start_y, end_y+1):
                        cave[y][start_x-min_x] = '#'
                else:
                    for y in range(end_y, start_y+1):
                        cave[y][start_x-min_x] = '#'
            elif start_y == end_y:  # we're going sideways
                if start_x < end_x:
                    for x in range(start_x, end_x+1):
                        cave[start_y][x-min_x] = '#'
                else:
                    for x in range(end_x, start_x+1):
                        cave[start_y][x-min_x] = '#'
            else:
                raise Exception("we r lost: {},{} -> {},{}".format(start_x, start_y, end_x, end_y))
    return cave

def drop_sand(cave, min_x, max_y, max_x):
    y = 0
    x = 500-min_x
    counter = 0
    while True:
        if y > max_y or x < 0 or x >= (max_x-min_x):
            return counter
        next_square = cave[y+1][x]
        if next_square == '.':
           y += 1
        else:
            if cave[y+1][x-1] == '.':  # if left empty, shift left
                y += 1
                x -= 1
            elif cave[y+1][x+1] == '.':  # if right empty, shift right
                y += 1
                x += 1
            else:  # left and right full, leave it here
                cave[y][x] = 'o'
                x = 500 - min_x
                y = 0
                counter += 1
                print("Cave after round {}:".format(counter))
                for rnum, row in enumerate(cave):
                    print('{} {}'.format(rnum, ''.join(row)))




max_x = 0
max_y = 1
min_x = 9999
rocks = [line for line in open(ifile, 'r').read().split('\n')]
for rock in rocks:
    segments = rock.split(' -> ')
    for segment in segments:
        x = int(segment.split(',')[0])
        y = int(segment.split(',')[1])
        max_x = x if x > max_x else max_x
        max_y = y if y > max_y else max_y
        min_x = x if x < min_x else min_x
cave = [['.'] * (max_x - min_x + 1) for i in range(0, max_y+1)]
cave[0][500-min_x] = '+'

cave = draw_rocks(cave, rocks, min_x)
print("Initial Cave")
for rnum, row in enumerate(cave):
    print('{} {}'.format(rnum, ''.join(row)))

print("Part 1: {}".format(drop_sand(cave, min_x, max_y, max_x)))




