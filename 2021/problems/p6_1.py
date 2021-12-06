class Lanternfish():
    def __init__(self, age):
        self.age = age

    def __repr__(self):
        return '{}'.format(self.age)

    def tick(self):
        self.age -= 1
        if self.age == -1:
            self.age = 6
            return Lanternfish(8)
        return None


input = open('../data/p6_data.txt', 'r')
# input = open('../data/p6_test_data.txt', 'r')
fish_in = input.read().split(',')
fish_in = [int(x) for x in fish_in]

fish = []
for f in fish_in:
    fish.append(Lanternfish(f))

for tick in range(0, 80):
    new_spawn = []
    for f in fish:
        spawn = f.tick()
        if spawn:
            new_spawn.append(spawn)
    fish += new_spawn

print(len(fish))