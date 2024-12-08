import sys
import itertools
sys.setrecursionlimit(10**6)

def test_operation_combo(result, input, operators):
    pass

def validate_equation(result, inputs) -> bool:
    num_operators = len(inputs) - 1
    operator_combinations = itertools.product(['+', '*'], repeat=num_operators)
    for combo in operator_combinations:
        running_total = inputs[0]
        for i in range(1, len(inputs)):
            match combo[i-1]:
                case '+':
                    running_total += inputs[i]
                case '*':
                    running_total *= inputs[i]
            if running_total > result:
                break
        if running_total == result:
            return True
    return False

def validate_equation_recursive(result, inputs, p2) -> bool:
    if len(inputs) == 1:
        return result == inputs[0]
    if validate_equation_recursive(result, [inputs[0] + inputs[1]] + inputs[2:], p2):
        return True
    if validate_equation_recursive(result, [inputs[0] * inputs[1]] + inputs[2:], p2):
        return True
    if p2 and validate_equation_recursive(result, [int(str(inputs[0]) + str(inputs[1]))] + inputs[2:], p2):
        return True
    return False


equations_f = open('input/7.txt', 'r')
equations = [(int(equation.split(':')[0]), [int(x) for x in equation.split(':')[1].split()]) for equation in equations_f.read().splitlines()]

total_calibration_result = 0
invalid_equations = []
for equation in equations:
    if validate_equation_recursive(equation[0], equation[1], False):
        total_calibration_result += equation[0]
    else:
        invalid_equations.append(equation)

print(f'Part 1: {total_calibration_result}')

concat_equations_total = 0
for equation in invalid_equations:
    if validate_equation_recursive(equation[0], equation[1], True):
        concat_equations_total += equation[0]

print(f'Part 2: {total_calibration_result} + {concat_equations_total} = {total_calibration_result+concat_equations_total}')
