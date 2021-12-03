input = open('../data/p1_data.txt', 'r')
depths = input.read().splitlines()
depths = [int(x) for x in depths]

inc = 0
prev = depths[0]
for depth in depths[1:]:
    if prev < depth:
        inc += 1
    prev = depth

# i = [inc for ]

print(inc)