from itertools import islice

def chunk(arr_range, arr_size):
    arr_range = iter(arr_range)
    return iter(lambda: tuple(islice(arr_range, arr_size)), ())
   
getPriorities = lambda l: [ord(x) - 96 if ord(x) >= 97 else ord(x) - (64 - 26) for x in l]
getIntersections = lambda ll: [list(set.intersection(*[set(y) for y in x]))[0] for x in ll]

lines = open('d3.txt','r').readlines()
halves = [(x[0:len(x)//2].strip(), x[len(x)//2::].strip()) for x in lines]
chunks = chunk([x.strip() for x in lines], 3)
answer1 = sum(getPriorities(getIntersections(halves)))
answer2 = sum(getPriorities(getIntersections(chunks)))
print(answer1, answer2)