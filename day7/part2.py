def part2(input):
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
        # Calculate total possible combinations using 3 operators (+, *, ||)
        # For n numbers, we need n-1 operators, hence 3^(n-1) combinations
        combinations = int(3** (len(inputRows[i]['nums']) - 1))
        leadingZeros = len(inputRows[i]['nums']) - 1

        # Try each possible combination of operators
        for p in range(0, combinations):
            # Convert to base-3 number for representing three operators
            # 0: Addition, 1: Multiplication, 2: Concatenation
            ops = []
            num = p
            for _ in range(leadingZeros):
                ops.append(num % 3)
                num //= 3
            ops = ops[::-1]  # Reverse to get correct order

            total = int(inputRows[i]['nums'][0])  # Start with first number

            # Apply operators based on base-3 digits
            for s in range(0, len(ops)):
                curr_num = int(inputRows[i]['nums'][s + 1])
                
                if ops[s] == 0:  # Addition
                    total += curr_num
                elif ops[s] == 1:  # Multiplication
                    total *= curr_num
                else:  # Concatenation (||)
                    # Convert numbers to strings, concatenate, then back to int
                    total = int(str(total) + str(curr_num))

            # If we found a valid combination that equals the target answer
            if total == inputRows[i]['ans']:
                allTotals += total
                break  # Move to next input row

    return allTotals

input_file='day7/input.txt'
with open(input_file, 'r') as file:
    puzzle_input = file.read()

res = part2(puzzle_input)
print(res)
