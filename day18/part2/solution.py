import networkx as nx

def parse_input(filename):
    # Read and parse input file into list of node coordinates
    with open(filename) as f:
        return [tuple(map(int, line.split(","))) 
                for line in f.read().strip().split("\n")]

def part2(nodes):
    # Find first node after 1024 that breaks path between (0,0) and (70,70)
    G = nx.grid_2d_graph(71, 71)
    
    # Remove first 1024 nodes
    for p in nodes[:1024]:
        G.remove_node(p)
    
    # Find breaking point
    for p in nodes[1024:]:
        G.remove_node(p)
        if not nx.has_path(G, (0, 0), (70, 70)):
            return p
    
    return None

nodes = parse_input('day18/input.txt')
print(part2(nodes))
