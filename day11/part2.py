from collections import defaultdict, Counter

def blink(rock):
    rock_str, rock_len = str(rock), len(str(rock))
    if rock == 0:
        return [1]
    elif rock_len % 2 == 0:
        mid = rock_len // 2
        return [int(rock_str[:mid]), int(rock_str[mid:])]
    else:
        return [2024 * rock]

def part2(puzzle_input):
    # Parse input into list of rock numbers
    rocks = puzzle_input.strip().split(" ")
    all_rock_count = Counter(map(int, rocks))
    
    # Perform 75 rounds of blinking transformations
    for _ in range(75):
        new_counts = defaultdict(int)
        for rock, count in all_rock_count.items():
            for new_rock in blink(rock):
                new_counts[new_rock] += count
        all_rock_count = new_counts
    return sum(all_rock_count.values())

puzzle_input = open('day11/input.txt', 'r').read()
print(part2(puzzle_input))