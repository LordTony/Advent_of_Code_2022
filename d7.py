tree = { "s": 0, "c": [] }
c, f, h = tree, [], 100000
for r in [r.strip().split(" ") for r in open("d7.txt","r").readlines()[2::]]:
    if r[0] == "dir":
        c["c"].append({ "n": r[1], "s": 0, "c": [], "p": c })
    elif r[0] not in ['$','dir']:
        c["s"] += int(r[0])
    elif r[-1] == '..':
        c = c["p"]
    elif r[1] == "cd":
        c = [x for x in c["c"] if x["n"] == r[2]][0]

def recurse(node, folders):
    returnme = node["s"] + sum([recurse(x, folders) for x in node["c"]])
    folders.append(returnme)
    return returnme

recurse(tree, f)
print(sum([s for s in f if s <= h]))
print(sorted([s for s in f if 700*h - f[-1] + s >= 300*h])[0])