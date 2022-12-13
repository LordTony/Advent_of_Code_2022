from functools import cmp_to_key
from numpy import prod

isInt = lambda i: isinstance(i, int)
bothAreLists = lambda p: isinstance(p[0], list) and isinstance(p[1], list)
typeJuggle = lambda p: p if (isInt(p[0]) and isInt(p[1])) or bothAreLists(p) \
    else [[p[0]], p[1]] if isInt(p[0]) else [p[0], [p[1]]]
ev = lambda x, i: eval(x.splitlines()[i])
k1, k2, raw = [[2]], [[6]], open("d13.txt","r").read()
data1 = [[ev(x,0), ev(x,1)] for x in raw.split("\n\n")]
data2 = [eval(x) for x in raw.splitlines() if x.strip() != '']
data2.extend([k1,k2])

def comp(left,right):
    [l,r] = typeJuggle([left,right])
    if isInt(l): return 1 if l > r else 0 if l == r else -1
    for i in range(max(len(l), len(r))):
        if(i >= len(l)): return -1
        if(i >= len(r)): return 1
        result = comp(l[i],r[i])
        if result != 0: return result
    return 0
        
print("part 1:", sum([i+1 for i,pair in enumerate(data1) if comp(*pair) == -1]))
print("part 2:", prod([i+1 for i,v in enumerate(sorted(data2, key=cmp_to_key(comp))) if v in [k1,k2]]))