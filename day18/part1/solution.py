import networkx as nx

def parse_input(filename):
    # Read and parse input file into list of node coordinates
    with open(filename) as f:
        return [tuple(map(int, line.split(","))) 
                for line in f.read().strip().split("\n")]

def part1(nodes):
    # Find shortest path length after removing first 1024 nodes
    G = nx.grid_2d_graph(71, 71)
    
    # Remove first 1024 nodes
    for p in nodes[:1024]:
        G.remove_node(p)
    
    return nx.shortest_path_length(G, (0, 0), (70, 70))

nodes = parse_input('day18/input.txt')
print(part1(nodes))