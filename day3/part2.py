import re

def part2(file_path):
    with open(file_path, 'r') as file:
        corrupted_memory = file.read()

    # Regular expressions for instructions
    mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    control_pattern = r"\b(do|don't)\(\)"
    
    # Find all mul and control instructions
    mul_matches = re.finditer(mul_pattern, corrupted_memory)
    control_matches = re.finditer(control_pattern, corrupted_memory)
    
    # Merge mul and control instructions in order of appearance
    instructions = []
    for match in mul_matches:
        instructions.append(('mul', int(match.group(1)), int(match.group(2)), match.start()))
    for match in control_matches:
        instructions.append((match.group(1), None, None, match.start()))
    instructions.sort(key=lambda x: x[3])  # Sort by position in the memory

    # Process instructions
    enabled = True  # mul instructions are initially enabled
    total_sum = 0
    for instruction in instructions:
        if instruction[0] == 'do':
            enabled = True
        elif instruction[0] == "don't":
            enabled = False
        elif instruction[0] == 'mul' and enabled:
            total_sum += instruction[1] * instruction[2]

    return total_sum

file_path = r'day3\input.txt'
result = part2(file_path)
print(result)
