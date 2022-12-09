steps = [x.split(" ") for x in open("d9.txt","r").read().splitlines()]
head, tail, c  = [0,0], [0,0], set([0,0])

closeEnough = lambda h,t: abs(h[0] - t[0]) < 2 and abs(h[1] - t[1]) < 2

def getCloser(h, t):
    t[0] += 1 if t[0] < h[0] else -1 if t[0] > h[0] else 0
    t[1] += 1 if t[1] < h[1] else -1 if t[1] > h[1] else 0
    
def help(index, direction, distance):
    head[index] += direction * distance
    while not closeEnough(head,tail):
        getCloser(head,tail)
        c.add(tuple(tail))

L = lambda d: help(0, -1, d)
R = lambda d: help(0,  1, d)
U = lambda d: help(1,  1, d)
D = lambda d: help(1, -1, d)      

for s in steps:
    eval(f"{s[0]}({s[1]})")
    
print(len(c))