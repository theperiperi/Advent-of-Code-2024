import re

def part1(file_path):
    with open(file_path, 'r') as file:
        corrupted_memory = file.read()
    
    # Regular expression for valid mul instructions
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    
    # Find all valid instructions
    matches = re.findall(pattern, corrupted_memory)
    
    # Calculate the sum of products
    total = sum(int(x) * int(y) for x, y in matches)
    return total

file_path = r'day3/input.txt'
result = part1(file_path)
print(result)
