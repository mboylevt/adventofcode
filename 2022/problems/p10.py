input = open('../data/p10_data.txt', 'r')
# input = open('../data/p10_test_small.txt', 'r')
# input = open('../data/p10_test_big.txt', 'r')
instructions = [line for line in input.read().split('\n')]

# Set stuff up
max_clock = 240
remaining_ccs = 0
register_x = 1
incrementer = None
signal = {}
crt = [['.']*40 for x in range(0,6)]

for tick in range(1, max_clock+1):
    if remaining_ccs == 0: # We need a new instruction
        if not instructions:
            print("Out of instructions")
            break
        ins = instructions.pop(0)
        match ins.split(' '):
            case ["noop"]:
                remaining_ccs = 1
            case ["addx", val]:
                remaining_ccs = 2
                incrementer = int(val)

    if (tick-1)%40 in [(register_x)-1, register_x, (register_x)+1]:
        crt[int((tick-1)/40)][(tick-1) % 40] = '#'

    signal[tick] = register_x * tick
    remaining_ccs -= 1
    if remaining_ccs == 0: # If it's time  inc, do it and reset sentinal to None
        if incrementer:
            register_x += incrementer
            incrementer = None

print("Part 1: {}".format(signal[20] + signal[60] + signal[100] + signal[140] + signal[180] + signal[220]))
print("Part 2: ")
for row in crt:
    print(''.join(row))