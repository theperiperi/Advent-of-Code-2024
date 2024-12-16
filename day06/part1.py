def part1(puzzle_input):
    # Parse the input into a 2D grid
    grid = [list(line) for line in puzzle_input.strip().split('\n')]
    
    # Define directions: up, right, down, left (clockwise)
    DIRECTIONS = [
        (-1, 0),   # Up
        (0, 1),    # Right
        (1, 0),    # Down
        (0, -1)    # Left
    ]
    
    # Find the initial guard position and direction
    def find_start():
        for r, row in enumerate(grid):
            for c, cell in enumerate(row):
                if cell in '^>v<':
                    # Map of starting directions
                    dir_map = {'^': 0, '>': 1, 'v': 2, '<': 3}
                    return r, c, dir_map[cell]
        return None
    
    # Check if a position is within grid and not an obstacle
    def is_valid_move(r, c):
        return (0 <= r < len(grid) and 
                0 <= c < len(grid[0]) and 
                grid[r][c] != '#')
    
    # Track visited positions
    visited = set()
    
    # Start the simulation
    r, c, direction = find_start()
    visited.add((r, c))
    
    while True:
        # Try to move forward in current direction
        dr, dc = DIRECTIONS[direction]
        next_r, next_c = r + dr, c + dc
        
        # If blocked, turn right
        if not is_valid_move(next_r, next_c):
            direction = (direction + 1) % 4
            continue
        
        # Move forward
        r, c = next_r, next_c
        visited.add((r, c))
        
        # Check if guard has left the mapped area
        if (r == 0 or r == len(grid) - 1 or 
            c == 0 or c == len(grid[0]) - 1):
            break
    return len(visited)

puzzle_input = open(r'day06/input.txt', 'r').read()
print(part1(puzzle_input))