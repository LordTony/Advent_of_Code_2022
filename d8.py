g, s, i = [x.strip() for x in open("d8.txt","r").readlines()], 0, 0

m = lambda l: max(l) if len(l) else "!"
def view(start, l):
    sum = 0
    for x in l:
        sum += 1
        if x >= start:
            break
    return sum
    
for x,l in enumerate(g):
    for y,v in enumerate(l):
        left, right, up, down = list(reversed(l[0:y])), l[y+1::], list(reversed([t[y] for t in g[0:x]])), [t[y] for t in g[x+1::]]
        s += v > min(m(left), m(right), m(up), m(down))
        i = max(i, view(v,left) * view(v,right) * view(v,up) * view(v,down))
print(s, i)