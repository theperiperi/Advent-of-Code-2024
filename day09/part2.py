import sys
from collections import deque

sys.setrecursionlimit(10**6)

def part2(puzzle_input):
    A = deque([])
    SPACE = deque([])
    file_id = 0
    FINAL = []
    pos = 0
    
    # Parse input
    for i,c in enumerate(puzzle_input.strip()):
        if i%2==0:
            A.append((pos, int(c), file_id))
            for _ in range(int(c)):
                FINAL.append(file_id)
                pos += 1
            file_id += 1
        else:
            SPACE.append((pos, int(c)))
            for _ in range(int(c)):
                FINAL.append(None)
                pos += 1

    # Process moves
    for (pos, sz, file_id) in reversed(A):
        for space_i,(space_pos, space_sz) in enumerate(SPACE):
            if space_pos < pos and sz <= space_sz:
                for i in range(sz):
                    assert FINAL[pos+i] == file_id, f'{FINAL[pos+i]=}'
                    FINAL[pos+i] = None
                    FINAL[space_pos+i] = file_id
                SPACE[space_i] = (space_pos + sz, space_sz-sz)
                break

    # Calculate result
    return sum(i*c for i,c in enumerate(FINAL) if c is not None)

infile = r'day09/input.txt'
input = open(infile).read().strip()
print(part2(input))