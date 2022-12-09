g, s = [x.strip() for x in open("d8.txt","r").readlines()], 0
m = lambda l: max(l) if len(l) else "!"
for x,l in enumerate(g):
    for y,v in enumerate(l):
        s += v > min(m(l[0:y]), m(l[y+1::]), m([t[y] for t in g[0:x]]), m([t[y] for t in g[x+1::]]))
        
print(s)