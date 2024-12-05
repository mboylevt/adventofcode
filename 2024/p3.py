import re
input = open('input/3.txt', 'r')
line = input.read()

def calculate_mul(commands):
    matches = re.findall('mul\(\d+,\d+\)', commands)
    running_total = 0
    for match in matches:
        nums = re.findall('\d+', match)
        running_total += (int(nums[0]) * int(nums[1]))
    return running_total

# Part 1
running_total = calculate_mul(line)
print("Part 1: {}".format(running_total))

# Part 2
do = r"do\(\)"
dont = r"don't\(\)"
mul = r"mul\((\d+),(\d+)\)"

enabled = True
running_total = 0
for x in re.finditer(f'{mul}|{do}|{dont}', line):
    if re.fullmatch(do, x.group()):
        enabled = True
    elif re.fullmatch(dont, x.group()):
        enabled = False
    elif enabled:
        running_total += int(x.group(1)) * int(x.group(2))

do = r"do\(\)"
dont = r"don't\(\)"
mul = r"mul\((\d+),(\d+)\)"
total = 0
enabled = True
for x in re.finditer(f'{do}|{dont}|{mul}', line):
    if re.fullmatch(do, x.group()):
        enabled = True
    elif re.fullmatch(dont, x.group()):
        enabled = False
    elif enabled:
        total += int(x.group(1)) * int(x.group(2))
print("Part 2: {}".format(total))
print("Part 2: {}".format(running_total))
