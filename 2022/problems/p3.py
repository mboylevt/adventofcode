input = open('../data/p3_data.txt', 'r')
# input = open('../data/p3_test_data.txt', 'r')
lines = input.read().splitlines()


def calc_priorities(dupes: {}):
    sum = 0
    for letter in dupes:
        if ord(letter) < 97:
            prio = ord((letter.lower())) - 96 + 26
            # print("Prio: letter {} -> {}".format(letter, prio))
            sum += prio
        else:
            prio = ord((letter.lower())) - 96
            # print("Prio: letter {} -> {}".format(letter, prio))
            sum += prio
    return sum


def find_duplicates(line) -> []:
    first = set(line[:int((len(line)/2))])
    second = set(line[int((len(line)/2)):])
    i_dupse = first.intersection(second)
    # print("dupes: {}".format(i_dupse))
    return i_dupse


# Part 1
prio_sum = 0
for line in lines:
    dupes = find_duplicates(line)
    prio_sum += calc_priorities(dupes)
print("Part 1: {}".format(prio_sum))

# Part 2
prio_sum = 0
for x in range(0, int(len(lines)/3)):
    badge = set(lines.pop()).intersection((set(lines.pop()))).intersection(set(lines.pop()))
    prio_sum += calc_priorities(badge)

print("Part 2: {}".format(prio_sum))