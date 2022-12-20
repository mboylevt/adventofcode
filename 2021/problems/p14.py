from collections import deque
input = open('../data/p14_data.txt', 'r')
# input = open('../data/p14_test_data.txt', 'r')

# Parse
lines = input.read().split('\n')
polymer = lines[0]
rule_str = lines[2:]
rules = {rule.split(' -> ')[0]: rule.split(' -> ')[1] for rule in rule_str}

abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def expand_polymer(polymer, rules):
    # Break polymer into pairs
    p_list = list(polymer)
    new_polymer = p_list[0] # Seed the first char to make looping easier later
    pairs = []
    for idx in range(0, len(p_list) - 1):
        pairs.append('{}{}'.format(p_list[idx], p_list[idx + 1]))

    for pair in pairs:
        to_append = pair[1]
        if pair in rules.keys():
            to_append = rules[pair] + pair[1]
        new_polymer += to_append
    return new_polymer


rounds = 40
for r in range(rounds):
    print("Round {}".format(r))
    polymer = expand_polymer(polymer, rules)

counts = {}
for letter in list(abc):

    if letter in polymer:
        counts[letter] = polymer.count(letter)
counts = sorted(counts.items(), key=lambda x:x[1], reverse=True)
print("Part 1: {}".format(counts[0][1] - counts[-1][1]))
I = 1