# just clear the shell so I don't have to keep doing it
#__import__("os").system("powershell clear")

isInt = lambda i: isinstance(i, int)
bothAreLists = lambda p: isinstance(p[0], list) and isinstance(p[1], list)
typeJuggle = lambda p: p if (isInt(p[0]) and isInt(p[1])) or bothAreLists(p) \
    else [[p[0]], p[1]] if isInt(p[0]) else [p[0], [p[1]]]
ev = lambda x, i: eval(x.splitlines()[i])
data = [[ev(x,0), ev(x,1)] for x in open("d13.txt","r").read().split("\n\n")]

def comp(pair):
    [l,r] = typeJuggle(pair)
    if isInt(l):
        #print("comparing ints", l, r)
        return 1 if l > r else 0 if l == r else -1
    #print("comparing arrays", l, r)
    for x in range(max(len(l), len(r))):
        if(x >= len(l)): return -1
        if(x >= len(r)): return 1
        result = comp([l[x],r[x]])
        if result != 0: return result
    return 0
        
print(sum([i+1 for i, pair in enumerate(data) if comp(pair) == -1]))