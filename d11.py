from re import findall 
from functools import reduce
from operator import mul

def operate(old, monkey, worryDivider):
    oprand = int(monkey["oprand"]) if monkey["oprand"].isnumeric() else old
    # I hate this worryDivider trick.
    return eval(f"{old}{monkey['op']}{oprand}") % worryDivider

def takeTurn(list, monkey, index, panic, container, worryDivider):
    items = monkey['items']
    while len(items):
        o = items[0]
        del items[0]
        n = operate(o, monkey, worryDivider) // (1 if panic else 3)
        id = monkey["fail" if n % monkey["mod"] else "pass"]
        list[id]['items'].append(n)
        container[index] += 1

def solve(rounds, panicMode): 
    monkeys, container = [], []
    for data in open("d11.txt","r").read().split("\n\n"):
        lines = data.splitlines()
        d = [int(x) for x in findall('[0-9]+', ''.join(lines[3::]))]
        cmd = lines[2].split("=")[1].strip().split(" ")
        monkeys.append({
            "items": [int(x) for x in findall('[0-9]+', lines[1])],
            "op": cmd[1],
            "oprand": cmd[2],         
            "mod": d[0], 
            "pass": d[1], 
            "fail": d[2] 
            })
        container.append(0)

    prod = lambda l: reduce(mul, l, 1)
    
    # Had to look up this trick.
    worryDivider = prod([x["mod"] for x in monkeys])
        
    for x in range(rounds):
        for i, monkey in enumerate(monkeys):
            takeTurn(monkeys, monkey, i, panicMode, container, worryDivider)
    return prod(sorted(container)[-2::])

print(solve(20, False), solve(10000, True))