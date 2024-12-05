input = open('input/2.txt', 'r')
lines = input.read().splitlines()

def eval_level(levels) -> int:
    # Increasing or decreasing?
    increasing = False
    if levels[0] < levels[1]:
        increasing = True
    unsafes = 0
    for i in range(0, len(levels)-1):
        cur = levels[i]
        next = levels[i+1]
        # If the delta > 2, return
        if abs(next - cur) > 3 or abs(next - cur) == 0:
            return 0
        if (next > cur) and not increasing:
            return 0
        elif (cur > next) and increasing:
            return 0
    return 1


### Main

safe_count = 0
levels = []
for line in lines:
    levels.append([int(x) for x in line.split()])

for level in levels:
    safe_count += eval_level(level)

print("Part 1: {}".format(safe_count))

safe_count_2 = 0
for level in levels:
    result = eval_level(level)
    if result:
        safe_count_2 += 1
        continue
    else:
        for i in range(0, len(level)):
            tmp_level = level.copy()
            tmp_level.pop(i)
            result = eval_level(tmp_level)
            if result:
                safe_count_2 += 1
                break


print("Part 2: {}".format(safe_count_2))