input = open('../data/p9_data.txt', 'r')
# input = open('../data/p9_test_data.txt', 'r')
lines = input.read().split('\n')
moves = [[line.split(' ')[0], int(line.split(' ')[1])]for line in lines]


class RopeKnot:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.pos = set()
        self.pos.add((0,0))

    def __repr__(self):
        return "Knot: {} {}".format(self.x, self.y)

    def mark(self):
        self.pos.add((self.x, self.y))

    def follow(self, knot):
        x,y = 0,0
        if abs(knot.x - self.x) > 1 or abs(knot.y - self.y) > 1:
            x = knot.x - self.x
            y = knot.y - self.y
        self.x += sorted([-1,x,1])[1]
        self.y += sorted([-1,y,1])[1]
        self.mark()


knots = [RopeKnot() for _ in range(10)]

for move in moves:
    head = knots[0]
    dir = move[0]
    q = move[1]
    while q > 0:
        if dir == 'U': head.y += 1
        elif dir == 'D': head.y -= 1
        elif dir == 'L': head.x -= 1
        elif dir == 'R': head.x += 1
        for i in range(9):
            knots[i+1].follow(knots[i])
        q -= 1

print(len(knots[1].pos))
print(len(knots[9].pos))