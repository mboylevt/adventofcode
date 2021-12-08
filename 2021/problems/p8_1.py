input = open('../data/p8_data.txt', 'r')
# input = open('../data/p8_test_data.txt', 'r')
lines = input.readlines()
count = 0
for line in lines:
    input, output = line.split(' | ')
    for digit in output.split():
        if len(digit) in (2, 3, 4, 7):
            count += 1

print(count)