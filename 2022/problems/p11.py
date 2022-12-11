input = open('../data/p11_data.txt', 'r')
# input = open('../data/p11_test_data.txt', 'r')

import re

class Monkey():
    def __init__(self, monkey_text):
        [number, items, operation, test_cond, test_t, test_f] = monkey_text.split('\n')
        self.monkey_id = int(re.findall(r'\d+', number)[0])
        items_str = re.findall(r'\d+', items)
        self.items = [int(item) for item in items_str]
        self.operator = operation[23]
        try:
            self.operation_scaler = int(re.findall(r'\d+', operation)[0])
        except:
            self.operation_scaler = 'old'
        self.test_div = int(re.findall(r'\d+', test_cond)[0])
        self.true_monkey = int(re.findall(r'\d+', test_t)[0])
        self.false_monkey = int(re.findall(r'\d+', test_f)[0])
        self.inspection_count = 0



    def __repr__(self):
        return "Simian {}: Items {}, operation {}, test {}, T {}, F {}".format(
            self.monkey_id,
            self.items,
            self.operator + ' ' + self.operation_scaler,
            self.test_div,
            self.true_monkey,
            self.false_monkey
        )


    def operate(self, starting_value):
        scalar = None
        if self.operation_scaler == 'old':
            scalar = starting_value
        else:
            scalar = self.operation_scaler
        match self.operator:
            case '*': return starting_value * scalar
            case '+': return starting_value + scalar
        raise Exception("Couldn't match operator")


    def test(self, item):
        return True if item % self.test_div == 0 else False

    def take_turn(self, monkeys):
        while True:
            if len(self.items) == 0: break
            self.inspection_count += 1
            item = self.items.pop(0)
            output = self.operate(item)
            output = int(output/3)
            if self.test(output):
                monkeys[self.true_monkey].items.append(output)
            else:
                monkeys[self.false_monkey].items.append(output)





input_monkeys = [line for line in input.read().split('\n\n')]
monkeys = [Monkey(monkey_input) for monkey_input in input_monkeys]
monkeys = {monkey.monkey_id: monkey for monkey in monkeys}

for round in range(0, 20):
    for monkey_id in monkeys.keys():
        monkeys[monkey_id].take_turn(monkeys)

inspections = sorted([monkey.inspection_count for monkey in monkeys.values()], reverse=True)
print("Part 1: {}".format(inspections[0] * inspections[1]))
