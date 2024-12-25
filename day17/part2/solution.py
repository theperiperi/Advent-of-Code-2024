import os

# Define the required functions if util is not available
def getlines(day):
    # Read lines from 'input.txt' located in the 'day17' folder
    input_path = os.path.join(day, 'input.txt')  # Assuming your 'day17' folder is in the current directory
    with open(input_path, 'r') as file:
        return file.read().splitlines()

def tokenedlines(line):
    # Placeholder for the actual implementation
    return line.split()

def Tuple(a, b):
    # Placeholder for the actual implementation
    return (a, b)

day = "day17"  # Folder name

# Read lines from 'input.txt' inside the 'day17' folder
lines = getlines(day)

# Processing the data (same as you had)
def getdata(line):
    # Check if the line contains the expected format
    if ": " in line:
        return line.split(": ")[1]
    return None  # Return None or handle the error as needed

# Extracting the values
a = int(getdata(lines[0]))  # Ensure lines[0] is valid
b = int(getdata(lines[1]))  # Ensure lines[1] is valid
c = int(getdata(lines[2]))  # Ensure lines[2] is valid
program = [int(x) for x in getdata(lines[4]).split(",")] if getdata(lines[4]) else []

# Function definitions (same as you had)
def combo(a, b, c, value):
    if value < 4:
        return value
    if value == 4:
        return a
    if value == 5:
        return b
    if value == 6:
        return c
    return None

def eval(a, b, c, ip, program):
    opcode = program[ip]
    arg = program[ip+1]
    comb = combo(a, b, c, arg)
    if opcode == 0:
        num = a
        denom = pow(2, comb)
        return (None, num // denom, b, c, ip + 2)
    elif opcode == 1:
        return (None, a, b ^ arg, c, ip + 2)
    elif opcode == 2:
        return (None, a, comb % 8, c, ip + 2)
    elif opcode == 3:
        if a == 0:
            return (None, a, b, c, ip + 2)
        else:
            return (None, a, b, c, arg)
    elif opcode == 4:
        return (None, a, b ^ c, c, ip + 2)
    elif opcode == 5:
        return (comb % 8, a, b, c, ip + 2)
    elif opcode == 6:
        num = a
        denom = pow(2, comb)
        return (None, a, num // denom, c, ip + 2)
    elif opcode == 7:
        num = a
        denom = pow(2, comb)
        return (None, a, b, num // denom, ip + 2)

def run_program(a, b, c, program):
    ip = 0
    res = []
    while ip < len(program) - 1:
        (out, a, b, c, ip) = eval(a, b, c, ip, program)
        if out is not None:
            res.append(out)
    return res

def get_best_quine_input(program, cursor, sofar):
    for candidate in range(8):
        if run_program(sofar * 8 + candidate, 0, 0, program) == program[cursor:]:
            if cursor == 0:
                return sofar * 8 + candidate
            ret = get_best_quine_input(program, cursor - 1, sofar * 8 + candidate)
            if ret is not None:
                return ret
    return None

def parse_input(filename):
    # Read and parse input file into program instructions
    with open(filename) as fname:
        lines = fname.readlines()
        initial_a = int(lines[0].split(": ")[1])
        initial_b = int(lines[1].split(": ")[1])
        initial_c = int(lines[2].split(": ")[1])
        program = [int(x) for x in lines[4].split(": ")[1].split(",")]
        return initial_a, initial_b, initial_c, program

def part2(program):
    # Find quine input that generates program as output
    return get_best_quine_input(program, len(program) - 1, 0)

_, _, _, program = parse_input('day17/input.txt')
print(part2(program))