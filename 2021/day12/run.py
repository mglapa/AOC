
#fn = 'sample.txt'
fn = 'input.txt'

def load():
    with open(fn, 'r') as f:
        lines = f.readlines()

    for i in range(len(lines)):
        lines[i] = lines[i].rstrip().split('-')

    # Create dict where key is name of cave and
    # val stores list of connected caves
    graph = {}
    for a, b in lines:
        if a not in graph.keys():
            graph[a] = []
        if b  not in graph.keys():
            graph[b] = []

        graph[a].append(b)
        graph[b].append(a)

    return graph

# Recursive visit function for part 1
def visit(graph, n, visited):
    if n == 'end':
        return 1
    
    # Only track lower-case caves
    if n.islower():
        visited.append(n)
    
    total = 0
    # Visit all 'next' nodes that are elligible
    for nxt in graph[n]:
        if nxt not in visited:
            total += visit(graph, nxt, visited.copy())
    return total

# Count how many nodes have been visited twice
def count_twos(visited):
    count = 0
    for key, val in visited.items():
        if val == 2:
            count += 1
    return count

# Recursive visit function for part 2
def visit2(graph, n, visited):
    if n == 'end':
        return 1
    
    # Only track lower-case caves
    if n.islower():
        if n not in visited.keys():
            visited[n] = 0
        visited[n] += 1
    
    total = 0
    # Visit all 'next' nodes that are elligible
    for nxt in graph[n]:

        # Count how many nodes have been visited twice
        # If none have been visited twice, then the search is still 'allowed' 2 visits
        # Otherwise, it can not re-visit a node
        twos = count_twos(visited)
        allowed = 2 if twos==0 else 1
        if nxt not in visited.keys() or visited[nxt] < allowed:
            # Never allow start to be revisited
            if nxt == 'start':
                continue
            total += visit2(graph, nxt, visited.copy())
    return total

def part1():
    graph = load()

    visited = []
    total = visit(graph, 'start', visited.copy())

    print('Part 1: ', total)

def part2():
    graph = load()
    
    visited = {}
    total = visit2(graph, 'start', visited.copy())

    print('Part 2: ', total)

def main():
    
    part1()

    part2()


if __name__ == '__main__':
    main()    























