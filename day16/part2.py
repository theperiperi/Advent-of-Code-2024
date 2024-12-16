import sys
import heapq

# Parse the input grid into a 2D array and find start/end positions
def parse_input(puzzle_input):
    grid = [list(line) for line in puzzle_input.strip().split('\n')]
    start = None
    end = None
    
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'S':
                start = (i, j)
            elif grid[i][j] == 'E':
                end = (i, j)
    return grid, start, end

def is_inside(x, y, n, m):
    return 0 <= x < n and 0 <= y < m

def part2(puzzle_input):
    # Parse input and initialize variables
    grid, (sr, sc), (er, ec) = parse_input(puzzle_input)
    n, m = len(grid), len(grid[0])
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # up right down left

    # First Dijkstra pass - find shortest path from start to end
    queue = []
    seen = set()
    heapq.heappush(queue, (0, sr, sc, 1))
    dist = {}
    best = None

    while queue:
        d, r, c, dir = heapq.heappop(queue)
        if (r, c, dir) not in dist:
            dist[(r, c, dir)] = d
        if r == er and c == ec and best is None:
            best = d
        if (r, c, dir) in seen:
            continue
            
        seen.add((r, c, dir))
        dr, dc = dirs[dir]
        rr, cc = r + dr, c + dc
        
        if is_inside(cc, rr, n, m) and grid[rr][cc] != '#':
            heapq.heappush(queue, (d + 1, rr, cc, dir))
        heapq.heappush(queue, (d + 1000, r, c, (dir + 1) % 4))
        heapq.heappush(queue, (d + 1000, r, c, (dir + 3) % 4))

    # Second Dijkstra pass - find paths from end
    queue = []
    seen = set()
    for dir in range(4):
        heapq.heappush(queue, (0, er, ec, dir))
    dist2 = {}
    
    while queue:
        d, r, c, dir = heapq.heappop(queue)
        if (r, c, dir) not in dist2:
            dist2[(r, c, dir)] = d
        if (r, c, dir) in seen:
            continue
            
        seen.add((r, c, dir))
        dr, dc = dirs[(dir + 2) % 4]
        rr, cc = r + dr, c + dc
        
        if is_inside(cc, rr, n, m) and grid[rr][cc] != '#':
            heapq.heappush(queue, (d + 1, rr, cc, dir))
        heapq.heappush(queue, (d + 1000, r, c, (dir + 1) % 4))
        heapq.heappush(queue, (d + 1000, r, c, (dir + 3) % 4))

    # Find valid positions that match best path length
    valid_positions = set()
    for r in range(n):
        for c in range(m):
            for dir in range(4):
                if (r, c, dir) in dist and (r, c, dir) in dist2:
                    if dist[(r, c, dir)] + dist2[(r, c, dir)] == best:
                        valid_positions.add((r, c))
                        
    return len(valid_positions)

puzzle_input = open('day16/input.txt', 'r').read()
print(part2(puzzle_input))