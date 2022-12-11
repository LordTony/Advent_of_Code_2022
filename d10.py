r, o = 1, []

for i in [x.split() for x in open("d10.txt","r").read().splitlines()]:
    o.append(r)
    if len(i) > 1:
        o.append(r)
        r += int(i[1])
    
print(sum([i*o[i] for i in [19,59,99,139,179,219]]))

for i in range(240):
    if not i%40: print()
    print('#' if i%40 in [o[i]-1, o[i], o[i]+1] else '.', end='')