def change_freq(freq, line):
    sign = line[:1]
    ordinal = line[1:]
    if sign == '+':
        freq += int(ordinal)
    else:
        freq -= int(ordinal)
    return freq

f = open('../data/p1.data', 'r')

freq = 0
for line in f.readlines():
    freq = change_freq(freq, line)
    print("Freqency: {freq}".format(freq=freq))

f.close()