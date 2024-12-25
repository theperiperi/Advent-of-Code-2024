def parse_input(filename):
    # Read and parse input file into patterns and designs
    with open(filename) as f:
        input_text = f.read().strip()
        sections = input_text.split('\n\n')
        patterns = [p.strip() for p in sections[0].split(',')]
        designs = [d.strip() for d in sections[1].splitlines()]
        return patterns, designs

def count_pattern_ways(target, available_patterns, memo=None):
    # Counts all possible ways to make a target pattern
    if memo is None:
        memo = {}
    
    # Base cases
    if not target:  # Empty target has one way to make it
        return 1
    if target in memo:
        return memo[target]
    
    # Try each available pattern at the current position
    total_ways = 0
    for pattern in available_patterns:
        if target.startswith(pattern):
            remaining = target[len(pattern):]
            total_ways += count_pattern_ways(remaining, available_patterns, memo)
    
    memo[target] = total_ways
    return total_ways

def part2(patterns, designs):
    # Sum up the number of ways for each design
    total_ways = 0
    for design in designs:
        ways = count_pattern_ways(design, patterns)
        total_ways += ways
    return total_ways

patterns, designs = parse_input('day19/input.txt')
print(part2(patterns, designs))