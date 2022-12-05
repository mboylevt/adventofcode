input = open('../data/p5_data.txt', 'r')
# input = open('../data/p5_test_data.txt', 'r')
lines = input.read().splitlines()
import copy

class Command():
    def __init__(self, quantity, source, dest):
        self.quantity = quantity
        self.source = source
        self.dest = dest

    def __repr__(self):
        return "Move {} from {} to {}".format(self.quantity, self.source, self.dest)


def parse_input(input):
    doing_stacks = True
    for line in lines:
        if line[1] != '1':
            continue
        num_stacks = int(line.split(' ').pop())
        break
    # num_stacks = int((len(input[0])+1) / 4)
    stacks = [[] for i in range (0,num_stacks)]
    moves = []
    width = 4
    for line in input:
        # Parse stacks
        if doing_stacks:
            if line[1] == '1':
                doing_stacks = False
            else:
                crates = [line[i:i+width] for i in range(0,len(line),width)]
                for i in range(0,len(crates)):
                    if crates[i][1] != ' ':
                        stacks[i].insert(0, crates[i][1])
        # Parse moves
        else:
            if not line:
                continue
            command = line.split(' ')
            moves.append(Command(quantity=int(command[1]), source=int(command[3])-1, dest=int(command[5])-1))
            i = 1
    return stacks, moves


def process1(stacks, commands):
    for command in commands:
        for mv in range(0, command.quantity):
            stacks[command.dest].append(stacks[command.source].pop())
    return stacks

def process2(stacks, commands):
    for command in commands:
        chunk = stacks[command.source][len(stacks[command.source])-command.quantity:len(stacks[command.source])]
        stacks[command.dest].extend(chunk)
        stacks[command.source] = stacks[command.source][0:len(stacks[command.source])-command.quantity]
    return stacks

stacks, move_list = parse_input(lines)

p1_stacks = process1(copy.deepcopy(stacks), move_list)
p2_stacks = process2(copy.deepcopy(stacks), move_list)
print(''.join([stack.pop() for stack in p1_stacks]))
print(''.join([stack.pop() for stack in p2_stacks]))


