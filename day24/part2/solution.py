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

def part2(values, operations):
    # Solve part 2: Find swapped operations
    use_map = defaultdict(list)
    for op in operations:
        use_map[op[0]].append(op)
        use_map[op[2]].append(op)

    swapped = set()
    for operation in operations:
        left, op, right, result = operation
        # Skip first and last bits
        if result == 'z45' or left == 'x00':
            continue

        if op == 'XOR':
            if is_input(left):
                if not is_input(right):
                    swapped.add(result)
                if result[0] == 'z' and result != 'z00':
                    swapped.add(result)
                usage = use_map[result]
                using_ops = [o[1] for o in usage]
                if result != 'z00' and sorted(using_ops) != ['AND', 'XOR']:
                    swapped.add(result)
            else:
                if result[0] != 'z':
                    swapped.add(result)

        elif op == 'AND':
            if is_input(left):
                if not is_input(right):
                    swapped.add(result)
            usage = use_map[result]
            if [o[1] for o in usage] != ['OR']:
                swapped.add(result)

        elif op == 'OR':
            if is_input(left) or is_input(right):
                swapped.add(result)
            usage = use_map[result]
            using_ops = [o[1] for o in usage]
            if sorted(using_ops) != ['AND', 'XOR']:
                swapped.add(result)

    return ','.join(sorted(swapped))

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

lines = parse_input('input.txt')
values, operations = parse_operations(lines)
print(part2(values, operations))
