from numpy import sign

head, tail, c  = [0,0], [0,0], set([0,0])

def closeEnough(h,t):
    return abs(h[0] - t[0]) < 2 and abs(h[1] - t[1]) < 2

def getCloser(h, t):
    t[0] += sign(h[0] - t[0])
    t[1] += sign(h[1] - t[1])
    
def help(index, direction, distance):
    head[index] += direction * distance
    while not closeEnough(head,tail):
        getCloser(head,tail)
        c.add(tuple(tail))

L = lambda d: help(0, -1, d)
R = lambda d: help(0,  1, d)
U = lambda d: help(1,  1, d)
D = lambda d: help(1, -1, d)      

for s in [x.split(" ") for x in open("d9.txt","r").read().splitlines()]: 
    eval(f"{s[0]}({s[1]})")
    
print(len(c))