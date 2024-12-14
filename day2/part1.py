def part1(input_file):
    input = [list(map(int, line.split())) for line in open(input_file)]

    def is_safe_sequence(sequence):
        # Check if any pair of consecutive numbers in the sequence meets the condition
        return any(all(down < num2 - num1 < up for num1, num2 in zip(sequence, sequence[1:]))for down, up in [(0, 4), (-4, 0)])
    # Return the count of sequences that are safe
    return sum(is_safe_sequence(sequence) for sequence in input)

input_file = r"day2/input.txt"
print(part1(input_file))

