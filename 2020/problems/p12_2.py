input = open('../data/p12_data.txt', 'r')
# input = open('../data/p12_test_data.txt', 'r')
waypoint_x = 10
waypoint_y = 1
ship_x = 0
ship_y = 0


for direction in input:
    instruction = direction[0]
    magnitude = int(direction[1:])
    print('{} {}'.format(instruction, magnitude))
    if instruction == 'N':
        waypoint_y += magnitude
    elif instruction == 'S':
        waypoint_y -= magnitude
    elif instruction == 'E':
        waypoint_x += magnitude
    elif instruction == 'W':
        waypoint_x -= magnitude
    elif instruction == 'R':
        if magnitude == 90:
            tmp = waypoint_x
            waypoint_x = waypoint_y
            waypoint_y = tmp * -1
        elif magnitude == 180:
            waypoint_y *= -1
            waypoint_x *= -1
        elif magnitude == 270:
            tmp = waypoint_x
            waypoint_x = waypoint_y * -1
            waypoint_y = tmp
    elif instruction == 'L':
        if magnitude == 270:
            tmp = waypoint_x
            waypoint_x = waypoint_y
            waypoint_y = tmp * -1
        elif magnitude == 180:
            waypoint_y *= -1
            waypoint_x *= -1
        elif magnitude == 90:
            tmp = waypoint_x
            waypoint_x = waypoint_y * -1
            waypoint_y = tmp
    elif instruction == 'F':
        for x in range(0, magnitude):
            ship_x += waypoint_x
            ship_y += waypoint_y
    print('\tWaypoint: {} {}'.format(waypoint_x, waypoint_y))
    print('\tShip: {} {}'.format(ship_x, ship_y))

print("Distance: {}".format(abs(ship_x) + abs(ship_y)))
