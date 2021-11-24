import re

input = open('../data/p4_data.txt', 'r')
raw_file = input.read()

chunks = raw_file.split('\n\n')

required_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

valid_ppt = 0

def date_validator(date, min, max):
    if not re.match('\d{4}', date):
        return False
    if int(date) < min or int(date) > max:
        return False
    return True

for chunk in chunks:
    data_dict = {}
    data = chunk.split()
    for d in data:
        k, v = d.split(':')
        data_dict[k] = v

    intersection = [x for x in required_keys if x in data_dict.keys()]

    # if we have all keys
    if len(intersection) == 7:
        birth_year = data_dict['byr']
        if not date_validator(birth_year, 1920, 2002):
            continue

        issue_year = data_dict['iyr']
        if not date_validator(issue_year, 2010, 2020):
            continue

        expiration_year = data_dict['eyr']
        if not date_validator(expiration_year, 2020, 2030):
            continue

        height = data_dict['hgt']
        hgt_regex = re.compile(r'(\d+)(.*)')
        matches = hgt_regex.search(height)
        if len(matches.groups()) != 2:
            continue
        try:
            hgt_value = int(matches.groups()[0])
            units = matches.groups()[1]
        except:
            continue
        if units == 'cm':
            if hgt_value < 150 or hgt_value > 193:
                continue
        elif units == 'in':
            if hgt_value < 59 or hgt_value > 76:
                continue
        else:
            # Units not in or cm
            continue

        hair_color = data_dict['hcl']
        if hair_color[0] != '#':
            continue
        hair_color = hair_color[1:]
        if (not re.match('[a-f0-9]{6}', hair_color)) and (len(hair_color) != 6):
            continue

        eye_color = data_dict['ecl']
        valid_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        if eye_color not in valid_colors:
            continue

        pid = data_dict['pid']
        if (not re.match('\d{9}', pid)) and (len(pid) != 9):
            continue

        print("Valid PPT!")
        for k in data_dict.keys():
            print('\t{} - {}'.format(k, data_dict[k]))
        print()
        valid_ppt += 1

print(valid_ppt)