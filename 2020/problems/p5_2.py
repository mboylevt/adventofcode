import math

input = open('../data/p5_data.txt', 'r')

seats = input.readlines()


def row_math(code, min, max):
    if len(code) == 1:
        if code[0] == 'F':
            return min
        return max
    delta = (max - min)/2
    if code[0] == 'F':
        return row_math(code[1:], min, int(min+delta))
    elif code[0] == 'B':
        return row_math(code[1:], int(math.ceil(min + delta)), max)
    else:
        raise Exception("Failed to parse")


def col_math(code, min, max):
    if len(code) == 1:
        if code[0] == 'L':
            return min
        return max
    delta = (max-min)/2
    if code[0] == 'L':
        return col_math(code[1:], min, int(min+delta))
    elif code[0] == 'R':
        return col_math(code[1:], int(math.ceil(min + delta)), max)
    else:
        raise Exception("Failed to parse")

highest_seat = 0
seat_ids = dict.fromkeys(range(8, 1016))

for seat in seats:
    row_code = seat[:7]
    column_code = seat[7:]
    row_number = row_math(row_code, 0, 127)
    col_number = col_math(column_code, 0, 7)
    seat_id = (row_number*8)+col_number
    # print("{} {} id: {}".format(row_number, col_number, (row_number*8)+col_number))
    if seat_id > 8 and seat_id < 1016:
        seat_ids[seat_id] = True

print(highest_seat)

for i in range(46, 915):
    if not seat_ids[i]:
        print(i)
        break
    # here = seat_ids[i]
    # next = seat_ids[i+1]

