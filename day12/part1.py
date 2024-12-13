def part1():
    grid = []
    with open('day12/input.txt', 'r') as f:
        for row in f.read().rstrip().split("\n"):
            grid.append(list(row))

    # Calculate price based on area * perimeter for each region
    price = 0
    visited = set()
    for y in range(0, len(grid)):
        for x in range(0, len(grid[0])):
            ch = grid[y][x]
            if not (y,x) in visited:
                area, perim, _ = find_region(grid, ch, y, x, visited)
                price += area * perim

    return price

def find_region(grid, ch, y, x, visited):
    area = 1
    perim = 0
    corners = 0  # Not used in part 1 but kept for compatibility
    visited.add((y,x))

    # get neighbors
    ch_up = grid_val(grid, y-1, x)
    ch_down = grid_val(grid, y+1, x)
    ch_left = grid_val(grid, y, x-1)
    ch_right = grid_val(grid, y, x+1)

    # Calculate perimeter
    if ch_up != ch:
        perim += 1
    if ch_down != ch:
        perim += 1
    if ch_left != ch:
        perim += 1
    if ch_right != ch:
        perim += 1
    
    # Recursively explore connected regions
    if ch_up == ch and not (y-1,x) in visited:
        a, p, c = find_region(grid, ch, y-1, x, visited)
        area += a
        perim += p
        corners += c
    if ch_down == ch and not (y+1,x) in visited:
        a, p, c = find_region(grid, ch, y+1, x, visited)
        area += a
        perim += p
        corners += c
    if ch_left == ch and not (y,x-1) in visited:
        a, p, c = find_region(grid, ch, y, x-1, visited)
        area += a
        perim += p
        corners += c
    if ch_right == ch and not (y,x+1) in visited:
        a, p, c = find_region(grid, ch, y, x+1, visited)
        area += a
        perim += p
        corners += c
    return([area, perim, corners])

def grid_val(grid, y, x):
    if 0 <= y < len(grid) and 0 <= x < len(grid[0]):
        return grid[y][x]
    else:
        return ' '

print("Part 1:", part1())