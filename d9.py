from numpy import sign

rope1, rope2 = [[0,0] for x in range(2)], [[0,0] for x in range(10)]
c1, c2 = set([(0,0)]), set([(0,0)])

def closeEnough(h,t):
    return abs(h[0] - t[0]) < 2 and abs(h[1] - t[1]) < 2

def getCloser(h, t):
    t[0] += sign(h[0] - t[0])
    t[1] += sign(h[1] - t[1])
    
def help(index, direction, distance, container, rope):
    for _ in range(distance):
        rope[0][index] += direction
        for i, k in enumerate(rope):
            if i == 0: continue
            if not closeEnough(rope[i-1], rope[i]):
                getCloser(rope[i-1], rope[i])
                if k is rope[-1]:
                    container.add(tuple(k))

L = lambda d,c,r: help(0, -1, d, c, r)
R = lambda d,c,r: help(0,  1, d, c, r)
U = lambda d,c,r: help(1,  1, d, c, r)
D = lambda d,c,r: help(1, -1, d, c, r)      

for s in [x.split(" ") for x in open("d9.txt","r").read().splitlines()]:
    exec(f"{s[0]}({s[1]},c1,rope1)\n{s[0]}({s[1]},c2,rope2)")
    
print(len(c1), len(c2))