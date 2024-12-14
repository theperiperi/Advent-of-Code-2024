DIRECTIONS_DIAGONAL = [
    (-1, -1),  # Up-left
    (-1, 1),   # Up-right
    (1, -1),   # Down-left
    (1, 1)     # Down-right
]

# Read and parse the input file into a grid of characters.
def read_file(filepath=r"day4/input.txt"):
    with open(filepath, "r") as file:
        return [line.strip() for line in file]

# Count occurrences of the letter 'X' followed by the sequence 'MAS' in any of the four diagonal directions.
def part1(grid):
    xmas_count = 0
    for row_index, row in enumerate(grid):
        for col_index, cell in enumerate(row):
            if cell != "X":  # Check only for cells containing 'X'
                continue
            # Check diagonally in all directions
            for delta_col, delta_row in DIRECTIONS_DIAGONAL:
                current_col, current_row = col_index + delta_col, row_index + delta_row
                diagonal_string = ""  # Collect characters along this diagonal
                while (
                    0 <= current_col < len(grid[0]) and  # Ensure within column bounds
                    0 <= current_row < len(grid) and    # Ensure within row bounds
                    len(diagonal_string) < 3           # Stop if we form a 3-character string
                ):
                    diagonal_string += grid[current_row][current_col]
                    current_col += delta_col
                    current_row += delta_row
                if diagonal_string == "MAS":  # Check if the string matches 'MAS'
                    xmas_count += 1
    return xmas_count

input_grid = read_file() 
grid = [[char for char in line] for line in input_grid]  # Convert lines to a character grid

xmas_count = part1(grid)
print(xmas_count)