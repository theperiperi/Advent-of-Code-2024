def parse_input(filename):
    # Read and parse input file into grid
    with open(filename) as f:
        return [list(line) for line in f.read().splitlines()]

def find_special_points(grid):
    # Find start and end points marked as 'S' and 'E'
    start = [(i,j) for i,line in enumerate(grid) for j,char in enumerate(line) if char=='S']
    end = [(i,j) for i,line in enumerate(grid) for j,char in enumerate(line) if char=='E']
    assert len(start)==1 and len(end)==1
    return start[0], end[0]

def cheat_endpoints(coords, track):
    # Find potential endpoints within range
    i,j = coords
    output = set()
    for di in range(-20,21):
        djmax = 20-abs(di)
        for dj in range(-djmax,djmax+1):
            if (i+di,j+dj) in track:
                output.add((i+di,j+dj))
    return output

def manhattan_distance(coord1, coord2):
    # Calculate Manhattan distance between two coordinates
    return sum(abs(i-j) for i,j in zip(coord1,coord2))

def part2(grid):
    # Find paths and count special conditions with Manhattan distance
    start, end = find_special_points(grid)
    track = {start: 0}
    cur = start
    curstep = 0
    
    # Find path to end
    while cur != end:
        curstep += 1
        i,j = cur
        for di,dj in [[-1,0],[0,-1],[0,1],[1,0]]:
            newi,newj = i+di,j+dj
            if (newi,newj) not in track and grid[newi][newj] in 'SE.':
                cur = (newi,newj)
                track[cur] = curstep
                break
    
    # Count special conditions using Manhattan distance
    count = 0
    for coords in track:
        potentials = cheat_endpoints(coords, track)
        for othercoords in potentials:
            if (track[othercoords] - track[coords] - 
                manhattan_distance(coords,othercoords) >= 100):
                count += 1
    return count

grid = parse_input('day20/input.txt')
print(part2(grid))