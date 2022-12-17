import pygame, sys
from pygame.locals import *
from time import sleep

d = [[(int(i.split(",")[0]),int(i.split(",")[1])) for i in x.split(" -> ")] \
    for x in open("d14.txt", "r").read().splitlines()]

sandPoint = (500,0)
minX, maxDepth, maxX, pxSize, sleepTime = 1000, 0, 0, 4, .002
grid, sand = set(), set()
BLACK, RED, BLUE, WHITE = (0,0,0), (255,0,0), (0,0,255), (255,255,255)
done = False

free = lambda node: node not in sand and node not in grid

def complete():
    print(len(sand))
    done = True
    
def translateDraw(window, item, color):
    pygame.draw.rect(window, color, Rect((item[0]-minX + 1)*pxSize, item[1]*pxSize, pxSize, pxSize))
    pygame.display.update()
    
def nextMove(g):
    down = (g[0], g[1]+1)
    left = (g[0]-1, g[1]+1)
    right = (g[0]+1, g[1]+1)
    if free(down): return down
    if free(left): return left
    if free(right): return right
    
# find grid bounds and setup grid
for shape in d:
    for i, point in enumerate(shape):
        if minX > point[0]: minX = point[0]
        if maxX < point[0]: maxX = point[0]
        if maxDepth < point[1]: maxDepth = point[1]
        if i > 0:
            curr, prev = shape[i], shape[i - 1]
            orientation = 0 if curr[0] != prev[0] else 1
            start = min(curr[orientation], prev[orientation])
            end = max(curr[orientation], prev[orientation])
            for x in range(start, end + 1):
                grid.add((curr[0], x) if orientation else (x, curr[1]))

# comment this loop out for part 1 solve
for x in range(-200, 800): grid.add((x, maxDepth+2))

# Draw Board
pygame.init()
pygame.display.set_caption('Sand Sand and More Sand')
window = pygame.display.set_mode(((maxX - minX + 2) * pxSize, (maxDepth + 5)* pxSize))
window.fill(WHITE)
translateDraw(window, sandPoint, BLUE)
for rock in grid:
    translateDraw(window, rock, BLACK)

# Start "Game" Loop
while True:
    if not done:
        grain = sandPoint
        next = nextMove(grain)
        while next is not None:
            if(grain[1] > maxDepth):
                complete()
                break
            grain = next
            next = nextMove(grain)
        sand.add(grain)
        translateDraw(window, grain, RED)
        pygame.display.update()
        sleep(sleepTime)
        if(grain == sandPoint): complete()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()