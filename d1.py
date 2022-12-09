sums = sorted([sum([int(y) for y in "".join(x).split("\n")]) for x in open("d1.txt", 'r').read().split("\n\n")])
print(sums[-1], sum(sums[-3::]))