import math

input = open('../data/p6_data.txt', 'r')

raw_input = input.read()
groups = raw_input.split('\n\n')

sum = 0
for group in groups:
    people = group.split('\n')
    if len(people) == 1:
        sum += len(people[0])
    else:
        common_ans = set(people[0])
        for person in people[1:]:
            common_ans = common_ans.intersection(person)
        sum += len(common_ans)

print(sum)