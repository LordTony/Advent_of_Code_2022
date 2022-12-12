import heapq

def addLinks(node, nodes, grid):
    nodes[node] = []
    for other in [(node[0], node[1]-1), (node[0], node[1]+1), (node[0]-1, node[1]), (node[0]+1, node[1])]:
        if canGo(node, other, grid):
            nodes[node].append(other)
        
def inBounds(node, grid):
    return node[0] >= 0 and node[1] >= 0 and node[0] < len(grid[0]) and node[1] < len(grid)
    
def getLetter(node, grid): 
    return grid[node[1]][node[0]]
    
def canGo(c, d, g): 
    if inBounds(d, g):
        start = getLetter(c, g)
        end = getLetter(d, g)    
        return (ord(start) + 1 >= ord(end) and ord(end) > 96) \
            or (getLetter(d, g) == 'E' and getLetter(c, g) in ['y','z']) \
            or getLetter(c, g) == 'S'
    return False
    
def solve(graph, starting_vertex):
    distances = {vertex: 1000000 for vertex in graph}
    distances[starting_vertex] = 0

    pq = [(0, starting_vertex)]
    while len(pq) > 0:
        current_distance, current_vertex = heapq.heappop(pq)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor in graph[current_vertex]:
            distance = current_distance + 1

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances[end]

## MAIN ##
g, nodes, start, end = open("d12.txt", "r").read().splitlines(), {}, (0,0), (0,0)

for y, row in enumerate(g):
    for x, letter in enumerate(row):
        addLinks((x,y), nodes, g)
        if letter == 'E': end = (x,y)
        if letter == 'S': start = (x,y)

print("part1:", solve(nodes, start))

startPositions = []
for y, row in enumerate(g):
    for x, letter in enumerate(row):
        if letter == 'a':
            startPositions.append((x,y))
            
print("part2", min([solve(nodes,x) for x in startPositions]))