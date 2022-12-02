input = open('../data/p2_data.txt', 'r')
lines = input.read().splitlines()

WIN = 6
DRAW = 3
LOSS = 0

ROCK_OPP = 'A'
PAPER_OPP = 'B'
SCISSORS_OPP = 'C'

ROCK_ME = 'X'
PAPER_ME = 'Y'
SCISSORS_ME = 'Z'

O_WIN = 'Z'
O_DRAW = 'Y'
O_LOSS = 'X'

score_map = {
    ROCK_ME: 1,
    PAPER_ME: 2,
    SCISSORS_ME: 3
}

def result_p1(opp, me):
    if opp == ROCK_OPP:
        if me == ROCK_ME:
            return DRAW
        elif me == PAPER_ME:
            return WIN
        elif me == SCISSORS_ME:
            return LOSS
        else:
            raise Exception("Invalid input - me: {} {}".format(opp, me))
    elif opp == PAPER_OPP:
        if me == ROCK_ME:
            return LOSS
        elif me == PAPER_ME:
            return DRAW
        elif me == SCISSORS_ME:
            return WIN
        else:
            raise Exception("Invalid input - me: {} {}".format(opp, me))
    elif opp == SCISSORS_OPP:
        if me == ROCK_ME:
            return WIN
        elif me == PAPER_ME:
            return LOSS
        elif me == SCISSORS_ME:
            return DRAW
        else:
            raise Exception("Invalid input - me: {} {}".format(opp, me))
    else:
        raise Exception("Invalid input - opp: {} {}".format(opp, me))


def result_p2(opp, outcome):
    if outcome == O_WIN:
        if opp == ROCK_OPP:
            return score_map[PAPER_ME] + WIN
        elif opp == PAPER_OPP:
            return score_map[SCISSORS_ME] + WIN
        elif opp == SCISSORS_OPP:
            return score_map[ROCK_ME] + WIN
        else:
            raise Exception("Invalid input - opp {} {}".format(opp, outcome))
    elif outcome == O_LOSS:
        if opp == ROCK_OPP:
            return score_map[SCISSORS_ME] + LOSS
        elif opp == PAPER_OPP:
            return score_map[ROCK_ME] + LOSS
        elif opp == SCISSORS_OPP:
            return score_map[PAPER_ME] + LOSS
        else:
            raise Exception("Invalid input - opp {} {}".format(opp, outcome))
    elif outcome == O_DRAW:
        if opp == ROCK_OPP:
            return score_map[ROCK_ME] + DRAW
        elif opp == PAPER_OPP:
            return score_map[PAPER_ME] + DRAW
        elif opp == SCISSORS_OPP:
            return score_map[SCISSORS_ME] + DRAW
        else:
            raise Exception("Invalid input - opp {} {}".format(opp, outcome))
    else:
        raise Exception("Invalid outcome: {} {}".format(opp, outcome))

# Part1
score = 0
for line in lines:
    opponent, mine = line.split()
    score += score_map[mine] + result_p1(opponent, mine)
print(score)

# Part2
score = 0
for line in lines:
    opponent, outcome = line.split()
    score += result_p2(opponent, outcome)
print(score)