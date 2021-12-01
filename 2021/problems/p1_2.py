# input = open('../data/p1_test_data.txt', 'r')
input = open('../data/p1_data.txt', 'r')
depths = input.read().splitlines()
depths = [int(x) for x in depths]

inc = 0
window_prev = depths[:3]
window_cur = depths[1:4]
for x, depth in enumerate(depths):
    print("Iteration {}".format(x))
    cur_sum = sum(window_cur)
    prev_sum = sum(window_prev)
    print("\tPrev Window: {}".format(window_prev))
    print("\tCur Window: {}".format(window_cur))
    print("\tPrev: {}\tCur: {}".format(prev_sum, cur_sum))
    if prev_sum < cur_sum:
        inc += 1
    if (x+4) == len(depths):
        break
    window_prev.pop(0)
    window_prev.append(window_cur[2])
    window_cur.pop(0)
    window_cur.append(depths[x+4])

print(inc)