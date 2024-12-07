import itertools
input = open('input/5.txt', 'r')
lines = input.read().splitlines()

rule_map = {}
text_break = lines.index("")
rules = lines[:text_break]
updates = lines[text_break+1:]
#parse rules
for rule in rules:
    page, before = rule.split('|')
    if page not in rule_map.keys():
        rule_map[page] = [before]
    else:
        rule_map[page].append(before)

middle_page_count = 0
invalid_updates = []

def validate_update(update) -> bool:
    valid = True
    for i in range(0, len(update)):
        if not valid:
            break
        current_page = update[i]
        before_pages = update[:i]
        after_pages = update[i + 1:]
        if current_page not in rule_map.keys() and after_pages:
            valid = False
        for page in before_pages:
            if page in rule_map.keys():
                if current_page not in rule_map[page]:
                    valid = False
    return valid

for update_str in updates:
    update = [x for x in update_str.split(',')]
    valid = validate_update(update)
    if valid:
        middle_idx = int(len(update)/2)
        value = int(update[middle_idx])
        middle_page_count += value
    else:
        invalid_updates.append(update)
print("Part 1: {}".format(middle_page_count))

fixed_update_middle = 0
# for update in invalid_updates:
#     print("Permutating update {}".format(update))
#     for permutation in list(itertools.permutations(update)):
#         if validate_update(permutation):
#             print("\tFixed: {}".format(permutation))
#             middle_idx = int(len(permutation) / 2)
#             value = int(permutation[middle_idx])
#             print("\tAdding: {}".format(value))
#             fixed_update_middle += value
#             break
for update in invalid_updates:
    print(f"Beginning book: {update}")
    flag_badData = False
    while not validate_update(update):
        flag_badData = True
        for i in range(len(update)):
            for j in range(len(update)):
                if i != j and update[j] in rule_map.keys() and update[i] in rule_map[update[j]] and i < j:
                    update[i], update[j] = update[j], update[i]
                    print(f"\tIntermediate book: {update}")
    print(f"Fixed book: {update}")
    if flag_badData:
        fixed_update_middle += int(update[len(update)//2])
print(f"Part 2: {fixed_update_middle}")
