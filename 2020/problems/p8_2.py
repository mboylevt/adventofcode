# input = open('../data/p8_test_data.txt', 'r')
from copy import deepcopy

input = open('../data/p8_data.txt', 'r')
instructions = input.readlines()
def process_instruction(line, pc, accumulator):
    operation, argument = line.split(' ')
    if operation == 'nop':
        return accumulator, pc + 1
    elif operation == 'acc':
        accumulator += int(argument)
        return accumulator, pc + 1
    elif operation == 'jmp':
        return accumulator, pc + int(argument)

pc = 0
def test_instruction_set(instructions):
    executed = {}
    accumulator = 0
    pc = 0
    while True:
        if pc in executed.keys():
            break
        executed[pc] = True
        if pc >= len(instructions):
            return accumulator
        accumulator, pc = process_instruction(instructions[pc].strip(), pc, accumulator)

    return -1

for idx, instruction in enumerate(instructions):
    print("Testing line {}".format(idx))
    temp_instructions = deepcopy(instructions)
    operation, argument = instruction.split(' ')
    if operation == 'acc':
        continue
    elif operation == 'nop':
        new_inst = 'jmp ' + argument
    elif operation == 'jmp':
        new_inst = 'nop ' + argument
    temp_instructions[idx] = new_inst
    acc = test_instruction_set(temp_instructions)
    if acc != -1:
        print(acc)
        break


