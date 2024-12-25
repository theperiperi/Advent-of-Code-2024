def parse_input(filename):
    # Read and parse input file into patterns and designs
    with open(filename) as f:
        input_text = f.read().strip()
        sections = input_text.split('\n\n')
        patterns = [p.strip() for p in sections[0].split(',')]
        designs = [d.strip() for d in sections[1].splitlines()]
        return patterns, designs

def can_make_pattern(target, available_patterns, memo=None):
    # Determines if a target pattern can be made from available patterns
    if memo is None:
        memo = {}
    
    # Base cases
    if not target:  # Empty target is always possible
        return True
    if target in memo:
        return memo[target]
    
    # Try each available pattern at the current position
    for pattern in available_patterns:
        if target.startswith(pattern):
            remaining = target[len(pattern):]
            if can_make_pattern(remaining, available_patterns, memo):
                memo[target] = True
                return True
    
    memo[target] = False
    return False

def part1(patterns, designs):
    # Count how many designs are possible to make from patterns
    possible_count = 0
    for design in designs:
        if can_make_pattern(design, patterns):
            possible_count += 1
    return possible_count

patterns, designs = parse_input('day19/input.txt')
print(part1(patterns, designs))