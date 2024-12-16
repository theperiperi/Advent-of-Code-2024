puzzle_input = open(r'day08/input.txt', 'r').read()
n, m = len(puzzle_input), len(puzzle_input[0])
output = [['.' for i in range(len(puzzle_input[j]))] for j in range(len(puzzle_input))]

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"


def dist(p1, p2):
    return p2[0] - p1[0], p2[1] - p1[1]

def isinside(x, y):
    return 0 <= x < n and 0 <= y < m

def pmap(data):
    print("\n".join("".join(c for c in line) for line in data))

def part1(puzzle_input):
    # Parse the input into a 2D grid
    grid = [list(line) for line in puzzle_input.strip().split('\n')]
    n, m = len(grid), len(grid[0])
    
    # Initialize output grid
    output = [['.' for _ in range(m)] for _ in range(n)]
    
    # All possible characters to look for
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    
    def dist(p1, p2):
        return p2[0] - p1[0], p2[1] - p1[1]
    
    def is_inside(x, y):
        return 0 <= x < n and 0 <= y < m
    
    # Process each character
    for c in chars:
        if c in puzzle_input:
            # Find all positions of current character
            positions = []
            for i in range(n):
                for j in range(m):
                    if grid[i][j] == c:
                        positions.append((i, j))
            
            # Calculate reflections for each pair
            for i in range(len(positions)):
                for j in range(i + 1, len(positions)):
                    dx, dy = dist(positions[i], positions[j])
                    
                    # Mark reflection points
                    if is_inside(positions[j][0] + dx, positions[j][1] + dy):
                        output[positions[j][0] + dx][positions[j][1] + dy] = '#'
                    if is_inside(positions[i][0] - dx, positions[i][1] - dy):
                        output[positions[i][0] - dx][positions[i][1] - dy] = '#'
    
    # Count marked positions
    return sum(row.count('#') for row in output)

# Read input file and run solution
print(part1(puzzle_input))