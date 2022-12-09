s = open('d6.txt','r').read()
solve = lambda l: [i+l for i in range(len(s)) if len(set(s[i:i+l])) == l][0]
print(solve(4), solve(14))