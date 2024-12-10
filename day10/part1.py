def get_score_and_rating(grid, head):
    # Initialize counters for total paths and unique endpoints
    paths = 0
    endpoints = set()
    
    # Use a queue for breadth-first traversal starting from the head position
    queue = [head]
    while len(queue):
        current = queue.pop()
        # If we reach a 9, we've found a complete path and endpoint
        if grid[current] == 9:
            paths += 1
            endpoints.add(current)
            continue
            
        # Check all four adjacent positions (up, down, left, right)
        for d in (1+0j, -1+0j, 1j, -1j):  # Complex numbers for 2D grid movement
            next = current + d
            # Only follow path if next position exists and increases by exactly 1
            if next in grid and grid[next] == grid[current] + 1:
                queue.append(next)
                
    return [len(endpoints), paths]

def part1(puzzle_input):
    # Parse input into grid using complex numbers as coordinates
    # Real part (a) represents x-coordinate, Imaginary part (b) represents y-coordinate
    grid = {a+b*1j: int(c) for b,r in enumerate(puzzle_input.splitlines()) 
           for a,c in enumerate(r.strip())}
    
    # Find all starting positions (cells with value 0)
    trailheads = {p for p in grid if grid[p] == 0}
    
    # Calculate total unique endpoints by summing endpoints from all starting positions
    # Using zip to combine results and map to sum the first elements (endpoint counts)
    p1, _ = map(sum, zip(*(get_score_and_rating(grid, p) for p in trailheads)))
    return p1

puzzle_input = open('day10/input.txt', 'r').read()
print(part1(puzzle_input))