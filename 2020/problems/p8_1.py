# input = open('../data/p8_test_data.txt', 'r')
input = open('../data/p8_data.txt', 'r')
instructions = input.readlines()
executed = {}
accumulator = 0

def process_instruction(line, pc):
    global accumulator
    operation, argument = line.split(' ')
    if operation == 'nop':
        return pc + 1
    elif operation == 'acc':
        accumulator += int(argument)
        return pc + 1
    elif operation == 'jmp':
        return pc + int(argument)

pc = 0
while True:
    if pc in executed.keys():
        break
    executed[pc] = True
    pc = process_instruction(instructions[pc].strip(), pc)

print(accumulator)
