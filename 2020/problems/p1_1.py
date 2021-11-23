input = open('../data/p1_data.txt', 'r')

data = input.readlines()
for a in data:
    a = int(a.strip())
    for b in data:
        b = int(b.strip())
        if a == b:
            continue
        if a + b == 2020:
            print(a * b)
            exit()




