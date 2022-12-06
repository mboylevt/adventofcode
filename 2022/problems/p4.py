input = open('../data/p4_data.txt', 'r')
# input = open('../data/p4_test_data.txt', 'r')
lines = input.read().splitlines()


# Part 1
contain = 0
overlap = 0
for line in lines:
    first, second = line.split(',')
    fs, fe = first.split('-')
    ss, se = second.split('-')

    # Contains
    if int(fs) <= int(ss) and int(fe) >= int(se):
        contain += 1
        # print("First contains Second {} {}".format(first, second))
    elif int(ss) <= int(fs) and int(se) >= int(fe):
        contain += 1
        # print("Second contains First {} {}".format(first, second))

    # Overlaps
    first_set = set(range(int(fs), int(fe)+1))
    second_set = set(range(int(ss), int(se)+1))
    intersect = first_set.intersection((second_set))
    if first_set.intersection((second_set)):
        print("Overlap: {} {}".format(first, second))
        overlap += 1

print("Part 1: {}".format(contain))
print("Part 2: {}".format(overlap))
