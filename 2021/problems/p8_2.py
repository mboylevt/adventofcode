
def diff(first, second):
    f, s = frozenset(first), frozenset(second)
    return len((f | s) - (f & s))

def same(first, second):
    f, s = frozenset(first), frozenset(second)
    return len(f & s)


input = open('../data/p8_data.txt', 'r')
# input = open('../data/p8_test_data.txt', 'r')
lines = input.readlines()
sum = 0

for line in lines:
    input, output = line.split(' | ')
    segments = list(map(''.join, map(sorted, input.split())))
    output = list(map(''.join, map(sorted, output.split())))
    digits = {}
    for segment in segments:
        if len(segment) == 2:
            digits[1] = segment
        elif len(segment) == 3:
            digits[7] = segment
        elif len(segment) == 4:
            digits[4] = segment
        elif len(segment) == 7:
            digits[8] = segment
    for segment in segments:
        if len(segment) == 5:
            if diff(digits[1], segment) == 3:
                digits[3] = segment
            elif diff(digits[4], segment) == 3:
                digits[5] = segment
            else:
                digits[2] = segment
        elif len(segment) == 6:
            if same(digits[1], segment) == 1:
                digits[6] = segment
            elif same(digits[4], segment) == 4:
                digits[9] = segment
            else:
                digits[0] = segment
    inverse_digits = {value: str(key) for key, value in digits.items()}
    sum += int(''.join([inverse_digits[digit] for digit in output]))
#     for digit in output.split():
#         if len(digit) in (2, 3, 4, 7):
#             count += 1
#
print(sum)