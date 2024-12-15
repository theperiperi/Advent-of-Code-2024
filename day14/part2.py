robots = []

with open('day14/input.txt', 'r') as file:
    for line in file:
        line = line.split()
        robots.append(
                (tuple(int(n) for n in line[0].split('=')[1].split(',')),
                tuple(int(n) for n in line[1].split('=')[1].split(','))
                ))

def calcPos(robot, sec):
    (x,y), (dx,dy) = robot
    return ((x + sec * dx) % 101, (y + sec * dy) % 103)

def calcSafety(sec):
    q1 = q2 = q3 = q4 = 0
    for robot in robots:
        x, y = calcPos(robot, sec)
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

def view(sec):
    layout = [['.'] * 101 for _ in range(103)]
    for robot in robots:
        x, y = calcPos(robot, sec)
        layout[y][x] = 'X'
    for row in layout:
        print(''.join(row))
    
safety = [calcSafety(sec) for sec in range(101*103)]

for sec, _ in sorted(enumerate(safety), key = lambda x: x[1]):
    view(sec)
    break

print(f'Safety after 100 sec : {safety[100]}')
print(f'Seconds for tree     : {sec}')