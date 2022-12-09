# input = open('../data/p9_data.txt', 'r')
input = open('../data/p9_test_data.txt', 'r')
lines = input.read().split('\n')
moves = [[line.split(' ')[0], int(line.split(' ')[1])]for line in lines]
i = 1