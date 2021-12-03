input = open('../data/p12_data.txt', 'r')
# input = open('../data/p12_test_data.txt', 'r')
x = 0
y = 0
heading = 0
for direction in input:
    instruction = direction[0]
    magnitude = int(direction[1:])
    print('{} {}'.format(instruction, magnitude))

    if instruction == 'N':
        y += magnitude
    elif instruction == 'S':
        y -= magnitude
    elif instruction == 'E':
        x += magnitude
    elif instruction == 'W':
        x -= magnitude
    elif instruction == 'R':
        heading -= magnitude
        if heading < 0:
            heading = 360 + heading
    elif instruction == 'L':
        heading += magnitude
        if heading >= 360:
            heading = heading - 360
    elif instruction == 'F':
        if heading == 0:
            x += magnitude
        elif heading == 90:
            y += magnitude
        elif heading == 180:
            x -= magnitude
        elif heading == 270:
            y -= magnitude

print("Distance: {}".format(abs(x) + abs(y)))
