input = open('input/1.txt', 'r')
lines = input.read().splitlines()

left = []
right = []

for line in lines:
    line_arr = line.split()
    left.append(int(line_arr[0]))
    right.append(int(line_arr[1]))

left.sort()
right.sort()

delta = 0
similarity = 0

for i in range(0,len(left)):
    delta += abs(left[i] - right[i])
    similarity += left[i] * right.count(left[i])
print("Part 1: {}".format(delta))
print("Part 2: {}".format(similarity))
