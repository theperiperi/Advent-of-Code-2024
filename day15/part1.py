puzzle_input = open(r'day15/input.txt', 'r').read()

def addt(x, y):
	if len(x) == 2:
		return (x[0] + y[0], x[1] + y[1])
	return tuple(map(sum, zip(x, y)))

def part1(puzzle_input):
	# Parse input
	parts = puzzle_input.strip().split('\n\n')
	grid_lines = parts[0].split("\n")
	moves_str = parts[1]

	DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
	D = [">", "<", "v", "^"]

	moves = [DIRS[D.index(m)] for m in moves_str.replace("\n", "")]

	# Set up initial state
	walls = set()
	boxes = set()
	robot = None
	
	for i, line in enumerate(grid_lines):
		for j, ch in enumerate(line):
			if ch == "#":
				walls.add((i,j))
			if ch == "O":
				boxes.add((i, j))
			if ch == "@":
				robot = (i, j)

	def push(box, d):
		nxt = addt(box, d)
		if nxt in walls:
			return False
		if nxt in boxes:
			if not push(nxt, d):
				return False
		boxes.remove(box)
		boxes.add(nxt)
		return True

	# Process moves
	for move in moves:
		nxt = addt(robot, move)
		if nxt in walls:
			continue
		if nxt in boxes:
			if not push(nxt, move):
				continue
		assert nxt not in boxes
		robot = nxt

	# Calculate final score
	return sum(100 * box[0] + box[1] for box in boxes)

# Run solution
print(part1(puzzle_input))