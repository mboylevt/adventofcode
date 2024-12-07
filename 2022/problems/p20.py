input = open('../data/p20_data.txt', 'r')
# input = open('../data/p20_test_data.txt', 'r')
lines = input.read().splitlines()
starting_list = [int(x) for x in lines]
final_list = starting_list.copy()

delta_tracker = 0

for index, entry in enumerate(starting_list):
    new_index = (index + entry) % len(final_list)
    final_list.insert(new_index, final_list.pop(o))
