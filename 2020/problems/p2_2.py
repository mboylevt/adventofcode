input = open('../data/p2_data.txt', 'r')

data = input.readlines()
valid = 0

for line in data:
    line.strip()
    range, radix, pw = line.split(' ')

    # True things up
    min, max = range.split('-')
    radix = radix[0]
    min = int(min)
    max = int(max)

    # Check
    first = pw[min-1]
    second = pw[max-1]

    if ( (first == radix) ^ (second == radix) ):
        valid += 1

print(valid)