input = open('../data/p2_data.txt', 'r')

data = input.readlines()
valid = 0

for line in data:
    line.strip()
    range, radix, pw = line.split(' ')

    # True things up
    min, max = range.split('-')
    radix = radix[0]

    # Check
    occurance = pw.count(radix)
    if occurance >= int(min) and occurance <= int(max):
        valid += 1

print(valid)