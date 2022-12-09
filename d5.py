import re
import copy

chunk = lambda str, n: [str[i:i+n].strip() for i in range(0, len(str), n)]
raw = open('d5.txt','r').readlines()

stack1 = [[],[],[],[],[],[],[],[],[]] 
for r in reversed([chunk(x,4) for x in raw[0:8]]):
    for i, b in enumerate(r):
        if len(b) > 0:
            stack1[i].append(b[1])
moves = [[int(y) - 1 for y in re.search(r"(\d+).+(\d+).+(\d+)", x).groups()] for x in raw[10::]]
stack2 = copy.deepcopy(stack1)

def solve1(stack, moves):
    for [num,start,end] in moves:
        for x in range(num + 1):
            stack[end].append(stack[start].pop())
    return ''.join([x[-1] for x in stack])
        
def solve2(stack, moves):
    for [num,start,end] in moves:
        subStack = stack[start][-(num + 1):]
        del stack[start][-(num + 1):]
        for x in subStack:
            stack[end].append(x)
    return ''.join([x[-1] for x in stack])
    
print(solve1(stack1, moves), solve2(stack2, moves))