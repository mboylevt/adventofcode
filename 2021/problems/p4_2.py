# input = open('../data/p5_test_data.txt', 'r')
input = open('../data/p4_data.txt', 'r')
#

def parse_input(lines):
    numbers = [int(x) for x  in lines[0].split(',')]
    card_input = lines[1:]
    parsed_cards = []
    for card in card_input:
        parsed_card = []
        rows = card.split('\n')
        for row in rows:
            parsed_card.append([int(x) for x in row.split()])
        parsed_cards.append(parsed_card)
    return numbers, parsed_cards


def check_for_win(card, row, col):
    # Test column
    col_win = True
    for test_row in range(0, 5):
        if card[test_row][col] != 'X':
            col_win = False
            break
    if col_win:
        return True

    row_win = True
    for test_col in range (0, 5):
        if card[row][test_col] != 'X':
            row_win = False
            break
    if row_win:
        return True


def process_number(number):
    global bingo_cards
    win = False
    winning_cards = []
    winning_cidx = []
    for cardidx, card in enumerate(bingo_cards):
        found = False
        win = False
        for rowidx, row in enumerate(card):
            for colidx, entry in enumerate(card):
                if card[rowidx][colidx] == number:
                    found = True
                    card[rowidx][colidx] = 'X'
                    break
            if found == True:
                win = check_for_win(card, rowidx, colidx)
                break
        if win:
            winning_cards.append(card)
            winning_cidx.append(cardidx)
            print("Win on {}: Removing card: {}".format(number, bingo_cards[cardidx]))
    if len(winning_cards) > 0:
        for card in winning_cards:
            if len(bingo_cards) > 1:
                bingo_cards.remove(card)
        return len(winning_cards)
    return None

numbers, bingo_cards = parse_input(lines=input.read().split('\n\n'))
winning_cards = 0
last_card_check = len(bingo_cards)
for number in numbers:
    card = process_number(number)
    if card:
        print("We got a winner - Total cards {}, Winners {}".format(
            last_card_check, winning_cards))
        winning_cards += card
        if winning_cards == last_card_check:
            board_sum = 0
            card = bingo_cards[0]
            for rowidx, row in enumerate(card):
                for colidx, entry in enumerate(card):
                    if card[rowidx][colidx] != 'X':
                        board_sum += card[rowidx][colidx]
            print("Last Winner - Score: {}".format(board_sum * number))
            break
