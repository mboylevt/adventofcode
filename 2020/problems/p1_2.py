input = open('../data/p1_data.txt', 'r')

data = input.readlines()
for a in data:
    a = int(a.strip())
    for b in data:
        b = int(b.strip())
        if a == b:
            continue
        if a + b > 2020:
            continue
        for c in data:
            c = int(c.strip())
            if c == a or c == b:
                continue
            if a + b + c == 2020:
                print(a*b*c)
                exit()




