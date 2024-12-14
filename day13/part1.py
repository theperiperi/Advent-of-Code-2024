import re
import sympy as sym

def parse_input(filename):
    # Read and parse input file into list of button behaviors
    with open(filename) as fname:
        return fname.read().split("\n\n")

def solve_part1(behaviours):
    # Solve part 1: Find valid button combinations that reach prizes
    # Returns sum of weighted button presses (A*3 + B)
    regex_numbers = re.compile(r"Button A: X\+(\d{2}), Y\+(\d{2})\nButton B: X\+(\d{2}), Y\+(\d{2})\nPrize: X=(\d{3,5}), Y=(\d{3,5})")
    x,y = sym.symbols('x,y')
    total = 0

    for behaviour in behaviours:
        numbersmatch = re.match(regex_numbers, behaviour)
        if numbersmatch:
            AX, AY, BX, BY, PX, PY = map(int, numbersmatch.groups())
        
            eq1 = sym.Eq(x*AX + y*BX, PX)
            eq2 = sym.Eq(x*AY + y*BY, PY)
            result = sym.solve([eq1,eq2],(x,y))

            if type(result[x]) is sym.core.numbers.Rational or type(result[y]) is sym.core.numbers.Rational:
                pass
            elif result[x] > 100 or result[y] > 100:
                pass
            else:
                total += result[x]*3 + result[y]

    return int(total)

puzzle_input = parse_input(r'day13/input.txt')
print(solve_part1(puzzle_input))