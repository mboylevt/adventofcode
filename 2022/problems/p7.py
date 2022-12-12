input = open('../data/p7_data.txt', 'r')
# input = open('../data/p7_test_data.txt', 'r')
lines = input.read().splitlines()

def parse_input(lines):
    stack = [{}]
    for line in lines:
        match line.split():
            case ['$', 'cd', '/']:  stack = [stack[0]]
            case ['$', 'cd', '..']: stack.pop()
            case ['$', 'cd', dir]:  stack.append(stack[-1][dir])
            case ['$', 'ls']:       continue
            case ['dir', dir]:      stack[-1][dir] = {}
            case [size, fname]:     stack[-1][fname] = int(size)
    return stack

stack = parse_input(lines)
sizes = []


def get_total_sizes(file):
    if isinstance(file, int):
        return file
    total = sum(get_total_sizes(d) for d in file.values())
    sizes.append(total)
    return total


ts = get_total_sizes(stack[0]) - 40000000
print(sum(size for size in sizes if size <= 100000 ))
print(min((size for size in sizes if size >= ts )))
i = 1
