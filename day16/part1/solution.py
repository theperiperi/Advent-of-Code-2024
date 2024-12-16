import heapq

def parse_input(input_data):
    grid = input_data.strip().split("\n")
    start = None
    end = None
    
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == 'S':
                start = (x, y)
            elif cell == 'E':
                end = (x, y)
    return grid, start, end

#basically dijikstra
def part1(puzzle_input):
    grid, start, end = parse_input(puzzle_input)
    # Directions: East, North, West, South
    directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    direction_names = ['E', 'N', 'W', 'S']
    
    rows = len(grid)
    cols = len(grid[0])

    def is_within_bounds(x, y):
        return 0 <= x < cols and 0 <= y < rows and grid[y][x] != '#'

    # Priority queue for Dijkstra's algorithm
    pq = []
    heapq.heappush(pq, (0, start[0], start[1], 0))  # (cost, x, y, direction_index)

    # Minimum cost to reach each position and direction
    visited = set()

    while pq:
        cost, x, y, direction = heapq.heappop(pq)

        if (x, y, direction) in visited:
            continue
        visited.add((x, y, direction))

        # Check if we've reached the end
        if (x, y) == end:
            return cost

        # Move forward
        dx, dy = directions[direction]
        nx, ny = x + dx, y + dy
        if is_within_bounds(nx, ny):
            heapq.heappush(pq, (cost + 1, nx, ny, direction))

        # Rotate clockwise and counterclockwise
        for rotation in [-1, 1]:
            new_direction = (direction + rotation) % 4
            heapq.heappush(pq, (cost + 1000, x, y, new_direction))

    return -1  # If no path is found

puzzle_input = open('day16/input.txt', 'r').read()
result = part1(puzzle_input)
print(result)
