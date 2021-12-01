from copy import deepcopy


def check_for_sum(window, target):
    for idx, x in enumerate(window):
        test_window = deepcopy(window)
        test_window = test_window[idx+1:]
        running_sum = x
        addends = [x]
        for idy, y in enumerate(test_window):
            running_sum += y
            addends.append(y)
            if running_sum == target_sum:
                print("Found target: range {}".format(addends))
                print("Sum of Min/Max: {}".format(min(addends) + max(addends)))
                return True
            elif running_sum > target_sum:
                break
    return False


input = open('../data/p9_data.txt', 'r')
target_sum = 400480901

# input = open('../data/p9_test_data.txt', 'r')
# target_sum = 127

xmas = input.read().splitlines()
xmas = [int(x) for x in xmas]
found = False

# for idx, num in enumerate(xmas):
#     print("Evaluating {}".format(num))
#     if check_for_sum(xmas[idx:], target_sum):
#         found = True
#         break
found = check_for_sum(xmas, target_sum)
if not found:
    print("Fail")
