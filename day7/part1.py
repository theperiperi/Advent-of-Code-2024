def part1(input):
    # Dictionary to store parsed input rows
    inputRows = dict()
    input = input.split('\n')

    # Parse each line of input into answer and numbers
    for i in range(0, len(input)):
        ans = int(input[i].split(':')[0])  # Get the target answer before colon
        nums = input[i].split(' ')[1:]      # Get the list of numbers after the answer
        inputRows[i] = {
            'ans': ans,
            'nums': nums
        }

    allTotals = 0
    for i in inputRows.keys():
        # Calculate total possible combinations using 2 operators (+, *)
        # For n numbers, we need n-1 operators, hence 2^(n-1) combinations
        combinations = int(2** (len(inputRows[i]['nums']) - 1))
        leadingZeros = len(inputRows[i]['nums']) - 1

        # Try each possible combination of operators
        for p in range(0, combinations):
            # Convert number to binary string to represent operator choices
            # 0 represents addition, 1 represents multiplication
            binaryStr = str(bin(p)[2:]).zfill(leadingZeros)
            total = int(inputRows[i]['nums'][0])  # Start with first number

            # Apply operators based on binary string
            for s in range(0, len(binaryStr)):
                if binaryStr[s] == '0':  # Addition
                    total += int(inputRows[i]['nums'][s + 1])
                if binaryStr[s] == '1':  # Multiplication
                    total *= int(inputRows[i]['nums'][s + 1])

            # If we found a valid combination that equals the target answer
            if total == inputRows[i]['ans']:
                allTotals += total
                break  # Move to next input row

    return allTotals

input_file='day7/input.txt'
with open(input_file, 'r') as file:
    puzzle_input = file.read()

res = part1(puzzle_input)
print(res)