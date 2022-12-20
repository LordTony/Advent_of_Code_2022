from dijkstar import Graph, find_path

class Move:
    def __init__(self, name, distance, score):
        self.name = name
        self.distance = distance
        self.score = score
        
    def __repr__(self):
        return f'{self.name}: {self.score}'
        
def inputObj(line):
    n = __import__("re").findall('\d+|[A-Z]{2}', line)
    return {"node": n[0], "rate": int(n[1]), "nodes": n[2::]}

def toDict(arr):
    d = dict()
    for i in arr:
        d[i["node"]] = i
        del i["node"]
    return d

def findNBestMoves(closedValves, n, currentNode):
    timeLeft = currentNode["time"]
    key = currentNode["node"]
    moves = []
    for x in closedValves:
        path_info = find_path(g, key, x)
        moves.append(Move(x, path_info.total_cost, (timeLeft - path_info.total_cost) * valves[x]["rate"]))
    return moves if len(moves) <= n else sorted(moves, key=lambda x: x.score)[-n::]
    
def recurse(closedValves, branchFactor, currentNode):
    for move in findNBestMoves(closedValves, branchFactor, currentNode):
        nextMoveTime = currentNode["time"] - (move.distance + 1)
        if nextMoveTime >= 0:
            removeMe = move.name
            closedValves.remove(removeMe)
            nextMove = {"node": removeMe, "time": currentNode["time"] - (move.distance + 1), "branches": []}
            currentNode["branches"].append(nextMove)
            recurse(closedValves, branchFactor, nextMove)
            closedValves.append(removeMe)

def getPaths(node, currentPath, allPaths):
    if len(node["branches"]) == 0:
        allPaths.append([*currentPath])
    for x in node["branches"]:
        currentPath.append((x["node"], x["time"], valves[x["node"]]["rate"]))
        returnme = getPaths(x, currentPath, allPaths)
        currentPath.remove((x["node"], x["time"], valves[x["node"]]["rate"]))
    return allPaths

valves = toDict([inputObj(x) for x in open('d16.txt','r').readlines()])

g = Graph()
for x in valves:
    for next in valves[x]["nodes"]:
        g.add_edge(x, next, 1)

#part2 = False
part2 = True
closedValves = [x for x in valves if valves[x]["rate"] > 0]
tree = { "node": 'AA', "time": 26 if part2 else 30, "branches": [] }
recurse(closedValves, 5, tree)

maxFlow = 0
for path in getPaths(tree, [], []):
    pathRate = 0
    for node in path:
        pathRate += (node[1] * node[2])
    if pathRate > maxFlow:
        maxFlow = pathRate

print(maxFlow)
