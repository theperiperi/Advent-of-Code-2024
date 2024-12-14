from collections import defaultdict, deque

def parse_input(input_text):
    sections = input_text.strip().split("\n\n")
    rules = [tuple(map(int, line.split('|'))) for line in sections[0].splitlines()]
    updates = [list(map(int, line.split(','))) for line in sections[1].splitlines()]
    return rules, updates

def build_graph(rules):
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    
    for x, y in rules:
        graph[x].append(y)
        in_degree[y] += 1
        in_degree[x] += 0  # Ensure all nodes are in the in_degree dictionary
    
    return graph, in_degree

def is_valid_update(update, graph, in_degree):
    # Filter the graph for only pages in this update
    sub_graph = defaultdict(list)
    sub_in_degree = defaultdict(int)
    
    for x in update:
        sub_in_degree[x] = 0
    
    for x, neighbors in graph.items():
        if x in update:
            for y in neighbors:
                if y in update:
                    sub_graph[x].append(y)
                    sub_in_degree[y] += 1
    
    # Perform topological sort
    queue = deque([node for node in update if sub_in_degree[node] == 0])
    sorted_order = []
    
    while queue:
        node = queue.popleft()
        sorted_order.append(node)
        for neighbor in sub_graph[node]:
            sub_in_degree[neighbor] -= 1
            if sub_in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return sorted_order == update

def find_middle_page(update):
    n = len(update)
    return update[n // 2]  # Middle element

def part1(input_text):
    rules, updates = parse_input(input_text)
    graph, in_degree = build_graph(rules)
    
    total = 0
    for update in updates:
        if is_valid_update(update, graph, in_degree):
            total += find_middle_page(update)
    
    return total

input_text = open(r'day5/input.txt', 'r').read()
result= part1(input_text)
print(result)