from collections import Counter

def part2(input_file):
    input = open(input_file).readlines()
    left = [int(x.split()[0]) for x in input]
    right = [int(x.split()[1]) for x in input]
    freq = Counter(right)
    return (sum(num * freq[num] for num in left))

input_file=r"Advent-of-Code-2024/day1/input.txt"
print(part2(input_file))