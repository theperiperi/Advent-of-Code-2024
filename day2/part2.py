def part2(input_file):
    input = [list(map(int, line.split())) for line in open(input_file)]
    
    def is_safe_sequence(sequence):
        # The condition checks pairs of consecutive elements in the sequence, ensuring the difference falls within specific bounds
        return any(all(down < num2 - num1 < up for num1, num2 in zip(sequence, sequence[1:])) for down, up in [(0, 4), (-4, 0)])
    # Count how many sequences are safe after removing one element from each sequence
    return sum(any(is_safe_sequence(sequence[:i] + sequence[i+1:]) for i in range(len(sequence))) for sequence in input)

input_file = r"Advent-of-Code-2024/day2/input.txt"
print(part2(input_file))
