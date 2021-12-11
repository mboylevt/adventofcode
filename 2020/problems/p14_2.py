import re
import sys

def mask_it(original, mask):
    new = ''
    for index, val in enumerate(mask):
        if val != 'X':
            new += val
        else:
            new += original[index]
    return new

def generate_addresses(original_address, mask):
    addresses = []

    return addresses


input = open('../data/p14_data.txt', 'r')
# input = open('../data/p14_test_data.txt', 'r')
data = input.readlines()
memory = {}
mask = ''
memory_regex = re.compile(r'mem\[(\d+)\]')

for line in data:
    instruction, argument = line.split(' = ')
    argument = argument.strip()
    if instruction == 'mask':
        mask = argument
    else:
        address = bin(int(memory_regex.search(instruction).group(1)))[2:]
        address = ('0' * (36 - len(address))) + address
        addresses = generate_addresses(address, mask)
        # memory[address] = int(final_argument, 2)

sum = 0
for key in memory.keys():
    sum += memory[key]

print(sum)