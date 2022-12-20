import re

getManDist = lambda a,b: abs(a[0] - b[0]) + abs(a[1] - b[1])
d = [[int(y) for y in re.findall(r'-?\d+', x)] for x in open("d15.txt","r").readlines()]
snbs = [{"s": (x[0],x[1]), "b": (x[2], x[3]), "m": getManDist((x[0],x[1]),(x[2],x[3]))} for x in d]
beacons = set([i["b"] for i in snbs])

impossible = set()
line = 2000000

def getRangeOnTargetLine(target, sensor, mDist):
    yDist = abs(sensor[1] - target)
    xRange = mDist - yDist
    returnme = []
    if(mDist > yDist):
        returnme.append((sensor[0],target))
        for x in range(xRange):
            returnme.append((sensor[0] + (x + 1),target))
            returnme.append((sensor[0] - (x + 1),target))
    #print(yDist, sensor)
    return returnme

for x in snbs:
    for r in getRangeOnTargetLine(line, x["s"], x["m"]):
        if(r not in beacons):
            impossible.add(r)

mn, mx = 0, 4000000
def getJustOutOfReachSpots(sensor, mDist):
    s = set()
    m = mDist + 1
    n = 0
    while m >= 0:
        x1,y1 = sensor[0]+m, sensor[1]+n
        x2,y2 = sensor[0]+m, sensor[1]-n
        x3,y3 = sensor[0]-m, sensor[1]+n
        x4,y4 = sensor[0]-m, sensor[1]-n
        if(mn <= x1 <= mx and mn <= y1 <= mx): s.add((x1,y1))
        if(mn <= x2 <= mx and mn <= y2 <= mx): s.add((x2,y2))
        if(mn <= x3 <= mx and mn <= y3 <= mx): s.add((x3,y3))
        if(mn <= x4 <= mx and mn <= y4 <= mx): s.add((x4,y4))
        m -= 1
        n += 1
    return s

foundItem = (-1,-1)
found = False
for i, x in enumerate(snbs):
    # progress report
    print(f"checking {i + 1} of {len(snbs)}")
    for checkme in getJustOutOfReachSpots(x["s"],x["m"]):
        for other in snbs:
            found = True
            if getManDist(checkme, other["s"]) <= other["m"]:
                found = False
                break
        if found:
            foundItem = checkme
            break
    if found: break

print(len(impossible))
print((4000000 * foundItem[0]) + foundItem[1])