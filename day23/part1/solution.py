import itertools
import networkx as nx

def parse_input(filename):
    # Read and parse input file into lines
    with open(filename) as f:
        return f.readlines()

def build_graph(input_lines):
    # Build graph from input lines
    G = nx.Graph()
    for line in input_lines:
        line = line.strip()
        a, b = line.split("-")
        G.add_edge(a, b)
    return G

def part1(graph):
    # Find sets of three and count those containing 't'
    setofthree = set()
    for a, b, c in itertools.combinations(graph.nodes(), 3):
        if a in graph[b] and a in graph[c] and b in graph[c]:
            setofthree.add((a+b+c))
    
    return sum(["t" in s[0]+s[2]+s[4] for s in setofthree])

lines = parse_input('day23/input.txt')
graph = build_graph(lines)
print(part1(graph))