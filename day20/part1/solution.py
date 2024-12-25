def parse_input(filename):
    # Read and parse input file into grid
    with open(filename) as f:
        return f.read().splitlines()

def find_special_points(grid):
    # Find start and end points marked as 'S' and 'E'
    start = [(i,j) for i,line in enumerate(grid) for j,char in enumerate(line) if char=='S']
    end = [(i,j) for i,line in enumerate(grid) for j,char in enumerate(line) if char=='E']
    assert len(start)==1 and len(end)==1
    return start[0], end[0]

def part1(grid):
    # Find paths and count special conditions
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
    
    # Count special conditions
    count = 0
    for i,j in track:
        for di,dj in [[-1,0],[0,-1],[0,1],[1,0]]:
            if ((i+di,j+dj) not in track and 
                (i+2*di,j+2*dj) in track and 
                track[(i+2*di,j+2*dj)]-track[(i,j)]>=102):
                count += 1
    return count

grid = parse_input('day20/input.txt')
print(part1(grid))