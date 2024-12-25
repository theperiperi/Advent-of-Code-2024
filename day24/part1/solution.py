from collections import defaultdict

def parse_input(filename):
    # Read and parse input file into lines
    try:
        with open(filename) as inf:
            lines = inf.readlines()
    except FileNotFoundError:
        with open(f"day24/{filename}") as inf:
            lines = inf.readlines()
    return [l.strip() for l in lines]

def is_input(operand):
    # Check if operand is an input value
    return operand[0] in 'xy'

def do_op(left, op, right):
    # Perform operation between two values
    if op == 'AND':
        return left and right
    if op == 'OR':
        return left or right
    if op == 'XOR':
        return left ^ right
    raise Exception()

def apply_operations(values, operations):
    # Apply all operations in sequence
    mem = dict(**values)

    while True:
        did_operation = False

        for op in operations:
            if op[3] in mem:
                continue
            if op[0] not in mem or op[2] not in mem:
                continue

            mem[op[3]] = do_op(mem[op[0]], op[1], mem[op[2]])
            did_operation = True

        if not did_operation:
            break

    return mem

def sum_zvalues(results):
    # Calculate sum of z-values in results
    z_keys = sorted([k for k in results if k.startswith('z')])[::-1]
    result = 0
    for k in z_keys:
        result <<= 1
        result += results[k]
    return result

def parse_operations(lines):
    # Parse input lines into values and operations
    values = {}
    operations = []
    for line in lines:
        if ':' in line:
            name, rest = line.split(':')
            value = int(rest.strip())
            values[name] = value
        elif '->' in line:
            parts = line.split(' ')
            op = (parts[0], parts[1], parts[2], parts[4])
            operations.append(op)
    return values, operations

def part1(values, operations):
    # Solve part 1: Apply operations and sum z-values
    results = apply_operations(values, operations)
    return sum_zvalues(results)

lines = parse_input('input.txt')
values, operations = parse_operations(lines)
print(part1(values, operations))