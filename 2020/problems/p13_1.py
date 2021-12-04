import sys

input = open('../data/p13_data.txt', 'r')
# input = open('../data/p13_test_data.txt', 'r')

data = input.readlines()
departure_time = int(data[0])
busses = list(filter(('x').__ne__, data[1].split(',')))
busses = [int(x) for x in busses]

best_bus = 0
best_pickup_time = 999999999999999
for bus in busses:
    first_available_pickup = int(departure_time / bus)*bus + bus
    if first_available_pickup < best_pickup_time:
        best_pickup_time = first_available_pickup
        best_bus = bus

print('{}'.format((best_pickup_time - departure_time) * best_bus))



