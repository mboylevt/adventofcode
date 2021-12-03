# input = open('../data/p2_test_data.txt', 'r')
input = open('../data/p2_data.txt', 'r')
lines = input.read().splitlines()

hpos = 0
depth = 0

for line in lines:
    direction, qty = line.split(' ')
    qty = int(qty)
    if direction == 'forward':
        hpos += qty
    elif direction == 'down':
        depth += qty
    elif direction == 'up':
        depth -= qty
    else:
        raise IOError("could not parse")

print('Depth: {} Hpos: {}'.format(depth, hpos))
print(depth * hpos)