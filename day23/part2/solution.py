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

def part2(graph):
    # Find max clique and return as sorted string
    clique = max(nx.find_cliques(graph), key=len)
    return ",".join(sorted(list(clique)))

lines = parse_input('day23/input.txt')
graph = build_graph(lines)
print(part2(graph))
