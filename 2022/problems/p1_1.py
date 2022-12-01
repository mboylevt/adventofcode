input = open('../data/p1_data.txt', 'r')
lines = input.read().splitlines()

elves = []
calories = 0
for line in lines:
    if not line:
        elves.append(calories)
        calories = 0
    else:
        calories += int(line)
print(sum(sorted(elves)[-3:]))
