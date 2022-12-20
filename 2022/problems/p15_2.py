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


maxTarget = 4000000

rx = 0
ry = 0
for target in range(maxTarget):
    segments = []
    for l in lines:
        s,_,dist = l
        x,y = s
        a = dist - abs(target-y)
        if(a>=0):
            seg = (max(0,x-a),min(maxTarget,x+a))
            segments.append(seg)
    segments = sorted(segments)
    total = 0
    s,e = segments[0]
    for i in range(1, len(segments)):
        ns,ne = segments[i]
        if(ns>e): #different segment
            s,e = ns,ne
            ry = target
            rx=ns-1

            break
        else:
            e = max(e,ne)
    else:
        continue
    break


print(rx,ry,ry+ rx*4000000)