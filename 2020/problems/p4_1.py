input = open('../data/p4_data.txt', 'r')
raw_file = input.read()

chunks = raw_file.split('\n\n')

required_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

valid_ppt = 0

for chunk in chunks:
    data_dict = {}
    data = chunk.split()
    for d in data:
        k, v = d.split(':')
        data_dict[k] = v

    intersection = [x for x in required_keys if x in data_dict.keys()]
    if len(intersection) == 7:
        valid_ppt += 1

print(valid_ppt)