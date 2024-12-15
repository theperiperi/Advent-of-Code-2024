def addt(x, y):
	if len(x) == 2:
		return (x[0] + y[0], x[1] + y[1])
	return tuple(map(sum, zip(x, y)))

def left(pos):
	return (pos[0], pos[1]-1)

def right(pos):
	return (pos[0], pos[1]+1)

def part2(puzzle_input):
	# Parse input
	parts = puzzle_input.strip().split('\n\n')
	grid_lines = parts[0].split("\n")
	moves_str = parts[1]

	DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
	D = [">", "<", "v", "^"]

	moves = [DIRS[D.index(m)] for m in moves_str.replace("\n", "")]

	# Set up initial state with double-width grid
	walls = set()
	boxes = set()
	robot = None
	
	for i, line in enumerate(grid_lines):
		for j, ch in enumerate(line):
			j *= 2
			if ch == "#":
				walls.add((i,j))
				walls.add((i,j+1))
			if ch == "O":
				boxes.add((i, j))
			if ch == "@":
				robot = (i, j)

	def push(box, d):
		assert box in boxes
		nxt = addt(box, d)
		if nxt in walls or right(nxt) in walls:
			return None
		if d[0]:
			# we are moving up/down
			if nxt in boxes:
				r = push(nxt, d)
				if r is None:
					return None
			if left(nxt) in boxes:
				r = push(left(nxt), d)
				if r is None:
					return None
			if right(nxt) in boxes:
				r = push(right(nxt), d)
				if r is None:
					return None
		if d[1] == 1:
			# we are pushing right
			if right(nxt) in boxes:
				r = push(right(nxt), d)
				if r is None:
					return None
		if d[1] == -1:
			# we are pushing left
			if left(nxt) in boxes:
				r = push(left(nxt), d)
				if r is None:
					return None
		boxes.remove(box)
		boxes.add(nxt)
		return True

	# Process moves
	for move in moves:
		for box in boxes:
			assert right(box) not in boxes
			assert right(box) not in walls
		nxt = addt(robot, move)
		if nxt in walls:
			continue

		if nxt in boxes:
			copy = {x for x in boxes}
			r = push(nxt, move)
			if r is None:
				boxes = copy
				continue
		elif left(nxt) in boxes:
			copy = {x for x in boxes}
			r = push(left(nxt), move)
			if r is None:
				boxes = copy
				continue
		assert nxt not in boxes
		assert left(nxt) not in boxes
		robot = nxt

	# Calculate final score
	return sum(100 * box[0] + box[1] for box in boxes)

puzzle_input = open(r'day15/input.txt', 'r').read()
print(part2(puzzle_input))