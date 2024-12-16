def part1(input_file):
    input = open(input_file).readlines()
    left = sorted(int(num.split()[0]) for num in input)
    right = sorted(int(num.split()[1]) for num in input)
    return(sum(abs(left[index] - right[index]) for index in range(len(left))))

input_file=r"day01/input.txt"
print(part1(input_file))