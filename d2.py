def solve(part):
    pts = {"A X":(4,3),"A Y":(8,4),"A Z":(3,8),"B X":(1,1),"B Y":(5,5),"B Z":(9,9),"C X":(7,2),"C Y":(2,6),"C Z":(6,7)}
    return sum([pts[x.strip()][part] for x in open("d2.txt","r").readlines()])
    
print(solve(0), solve(1))