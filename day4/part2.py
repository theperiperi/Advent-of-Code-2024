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

"""
Count cells containing the letter 'A' where diagonals from the 'A' form the 'XMAS' pattern:
- One diagonal is 'X' (top-left) -> 'M' -> 'A' -> 'S' (bottom-right)
- The other diagonal is 'X' (top-right) -> 'M' -> 'A' -> 'S' (bottom-left)
"""
def part2(grid):
    xmas_pattern_count = 0
    for row_index, row in enumerate(grid):
        for col_index, cell in enumerate(row):
            # Ensure the cell is 'A' and has enough space for diagonals
            if cell != "A" or col_index == 0 or row_index == 0 or \
               row_index == len(grid) - 1 or col_index == len(grid[0]) - 1:
                continue

            # Check surrounding diagonal elements
            top_right = grid[row_index - 1][col_index + 1]
            bottom_right = grid[row_index + 1][col_index + 1]
            top_left = grid[row_index - 1][col_index - 1]
            bottom_left = grid[row_index + 1][col_index - 1]

            # Check if diagonals form the 'XMAS' pattern
            if (top_right + bottom_left) in ("MS", "SM") and \
               (top_left + bottom_right) in ("MS", "SM"):
                xmas_pattern_count += 1
    return xmas_pattern_count


input_grid = read_file() 
grid = [[char for char in line] for line in input_grid]  # Convert lines to a character grid

# Part 2: Find 'XMAS' patterns centered on 'A'
xmas_pattern_count = part2(grid)
print(xmas_pattern_count)
