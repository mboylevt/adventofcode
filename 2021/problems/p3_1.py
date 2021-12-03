# input = open('../data/p3_test_data.txt', 'r')
input = open('../data/p3_data.txt', 'r')
lines = input.read().splitlines()

transpose = [list(row) for row in zip(*lines)]

gamma_str = ''
for line in transpose:
    if line.count('1') > line.count('0'):
        gamma_str += '1'
    else:
        gamma_str += '0'

epsilon_str = ''
for x in gamma_str:
    if x == '0':
        epsilon_str += '1'
    else:
        epsilon_str += '0'

gamma = int(gamma_str, 2)
epsilon = int(epsilon_str, 2)
print("Power consumption: {}".format(gamma*epsilon))
i = 1