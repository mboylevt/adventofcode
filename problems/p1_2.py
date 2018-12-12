def change_freq(freq, line):
    sign = line[:1]
    ordinal = line[1:]
    if sign == '+':
        freq += int(ordinal)
    else:
        freq -= int(ordinal)
    return freq



f = open('../data/p1.data', 'r')
data = f.readlines()
f.close()

freq = 0
seen_freqs = {}
while True:
    for line in data:
        freq = change_freq(freq, line)
        if freq in seen_freqs.keys():
            print("Repeat frequency: {}".format(freq))
            exit()
        else:
            seen_freqs[freq] = True

