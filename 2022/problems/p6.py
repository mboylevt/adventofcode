input = open('../data/p6_data.txt', 'r')
# input = open('../data/p6_test_data.txt', 'r')
lines = input.read().splitlines()
import copy


def convert(str):
    l = []
    return l[:0]



for line in lines:
    lst = [*line]
    buffer = []
    for idx, letter in enumerate(lst):
        buffer.append(letter)
        if len(buffer) == 14:
            if len(set(buffer)) == 14:
                print(idx+1)
                break
            buffer = buffer[1:]