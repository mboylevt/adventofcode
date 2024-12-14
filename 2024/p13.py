
import re
import sys
sys.setrecursionlimit(10**6)


def parse_input(ifile):
    f = open(ifile, 'r')
    games = [x for x in f.read().split('\n\n')]
    button_re = re.compile(r'X\+(\d+), Y\+(\d+)')
    prize_re = re.compile(r'X=(\d+), Y=(\d+)')
    arcade = []
    for game in games:
        sa, sb, sprize = game.split('\n')
        match_a = button_re.search(sa)
        match_b = button_re.search(sb)
        match_p = prize_re.search(sprize)

        g = [int(match_a.group(1)), int(match_a.group(2)), int(match_b.group(1)), int(match_b.group(2)), int(match_p.group(1)), int(match_p.group(2))]

        # a = (int(match_a.group(1)), int(match_a.group(2)))
        # b = (int(match_b.group(1)), int(match_b.group(2)))
        # prize = (int(match_p.group(1)), int(match_p.group(2)))

        arcade.append(g)
    return arcade

def solve(game, p2=False):
    xa, ya, xb, yb, xp, yp = game

    if (p2):
        xp += 10000000000000
        yp += 10000000000000

    b = (yp * xa - ya * xp) / (xa * yb - ya * xb)
    a = (xp - xb * b) / xa

    if int(b) != b or int(a) != a:
        return 0
    if not p2:
        if a > 100 or a < 0 or b > 100 or b < 0:
            return 0
    return a*3 + b

arcade = parse_input('input/13.txt')
tokens = 0
tokens_p2 = 0

for game in arcade:
    tokens += solve(game)
for game in arcade:
    tokens_p2 += solve(game, True)

print(f'Part 1: {int(tokens)}')
print(f'Part 2: {int(tokens_p2)}')