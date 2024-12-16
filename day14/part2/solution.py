def parse_robots(puzzle_input):
    # Parse each line into robot positions and velocities
    robots = []
    for line in puzzle_input.strip().splitlines():
        line = line.split()
        robots.append(
            (tuple(int(n) for n in line[0].split('=')[1].split(',')),  # position (x,y)
            tuple(int(n) for n in line[1].split('=')[1].split(',')))   # velocity (dx,dy)
        )
    return robots

def calc_pos(robot, sec):
    # Calculate robot position at given second
    (x,y), (dx,dy) = robot
    return ((x + sec * dx) % 101, (y + sec * dy) % 103)

def calc_safety(robots, sec):
    # Calculate safety score based on robot distribution in quadrants
    q1 = q2 = q3 = q4 = 0
    for robot in robots:
        x, y = calc_pos(robot, sec)
        if x < 50:
            if y < 51:
                q1 += 1
            elif y > 51:
                q2 += 1
        elif x > 50:
            if y < 51:
                q3 += 1
            if y > 51:
                q4 += 1
    return q1 * q2 * q3 * q4

def view(robots, sec):
    # Visualize robot positions at given second
    layout = [['.'] * 101 for _ in range(103)]
    for robot in robots:
        x, y = calc_pos(robot, sec)
        layout[y][x] = 'X'
    return layout

def part2(puzzle_input):
    # Parse input and get robots
    robots = parse_robots(puzzle_input)
    
    # Calculate safety scores for all possible positions
    safety = [calc_safety(robots, sec) for sec in range(101*103)]
    
    # Find second with minimum safety score
    min_safety_sec = min(enumerate(safety), key=lambda x: x[1])[0]
    
    return min_safety_sec

puzzle_input = open(r'day14/input.txt', 'r').read()
print(part2(puzzle_input))