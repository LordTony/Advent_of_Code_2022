solve = lambda l, func: sum([1 for x in l if func(*x)])
r = [[int(y) for y in __import__("re").split(r',|-', x)] for x in open("d4.txt","r").readlines()]
print(solve(r, lambda a,b,c,d: a >= c and b <= d or c >= a and d <= b))
print(solve(r, lambda a,b,c,d: a >= c and a <= d or c >= a and c <= b))