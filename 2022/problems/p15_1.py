input = open('../data/p15_data.txt', 'r')
# input = open('../data/p15_test_data.txt', 'r')

# Parse
lines = input.read().split('\n')

def parse(line):
    [s_line, b_line] = line.split(':')
    s_line = list(s_line)[12:]
    b_line = list(b_line)[24:]
    c_idx = s_line.index(',')
    sensor = (int(''.join(s_line[:c_idx])), int(''.join(s_line[c_idx+4:])))
    c_idx = b_line.index(',')
    beacon = (int(''.join(b_line[:c_idx])), int(''.join(b_line[c_idx+4:])))
    return [sensor, beacon, abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])]


lines = [parse(line) for line in lines]

target = 2000000
segments = []
for line in lines:
    s, _, distance = line
    x, y = s
    a = distance - abs(target-y)
    if a >= 0:
        segment = (x-a, x+a)
        print("Adding  {} {} {} {}".format(segment, a, s, distance))
        segments.append(segment)
segments = sorted(segments)
[print(i) for i in segments]
total = 0
start, end = segments[0]
for i in range(1, len(segments)):
    n_start, n_end = segments[i]
    if n_start > end:
        print("Size: {} {} {} {}".format(start, end, n_start, n_end))
        total = total + (end - start)
        start, end = n_start, n_end
    else:
        end = max(end, n_end)
print("size: {} {}".format(start, end))
total = total + (end - start)
print(total)