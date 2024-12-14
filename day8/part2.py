def part2(puzzle_input):
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
                    
                    # Mark all reflection points in the line
                    for k in range(0, max(n, m)):
                        if is_inside(positions[j][0] + k * dx, positions[j][1] + k * dy):
                            output[positions[j][0] + k * dx][positions[j][1] + k * dy] = '#'
                        if is_inside(positions[i][0] - k * dx, positions[i][1] - k * dy):
                            output[positions[i][0] - k * dx][positions[i][1] - k * dy] = '#'
    
    # Count marked positions
    return sum(row.count('#') for row in output)

puzzle_input = open(r'day8/input.txt', 'r').read()
print(part2(puzzle_input))
