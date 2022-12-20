import pygame, sys
from pygame.locals import *
from time import sleep

d = [[(int(i.split(",")[0]),int(i.split(",")[1])) for i in x.split(" -> ")] \
    for x in open("d14.txt", "r").read().splitlines()]

sandPoint = (500,0)
minX, maxDepth, maxX, pxSize, sleepTime, bottomY = 1000, 0, 0, 4, .001, 0
grid, sand, movedSand = set(), set(), set()
BLACK, RED, BLUE, WHITE, ORANGE = (0,0,0), (255,0,0), (0,0,255), (255,255,255), (255, 0xA5, 0)
done = False
part = 1
#part = 2
free = lambda node: node not in sand and node not in grid and (part == 1 or part == 2 and node[1] < bottomY)

def complete():
    print(len(sand))
    return True
        
def translateDraw(window, item, color):
    pygame.draw.rect(window, color, Rect((item[0] - minX + 2) * pxSize, item[1] * pxSize, pxSize, pxSize))
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

bottomY = maxDepth + 2

# Draw Board
pygame.init()
pygame.display.set_caption('Sand Sand and More Sand')
window = pygame.display.set_mode(((maxX - minX + 4) * pxSize, (maxDepth + 5)* pxSize))
window.fill(WHITE)
translateDraw(window, sandPoint, BLUE)
for rock in grid:
    translateDraw(window, rock, BLACK)

for x in range(maxX - minX, maxX + 4, [0,2,1][part]):
    translateDraw(window, (x, bottomY), BLUE if part == 1 else BLACK)

# Start "Game" Loop
while True:
    if not done:
        grain = sandPoint
        next = nextMove(grain)
        while next is not None:
            if next not in movedSand:
                translateDraw(window, next, RED)
                movedSand.add(next)
            if(part == 1 and grain[1] > maxDepth):
                done = complete()
                break
            grain = next
            next = nextMove(grain)
        if not done: 
            sand.add(grain)
            translateDraw(window, grain, ORANGE)
        pygame.display.update()
        sleep(sleepTime)
        if(grain == sandPoint): done = complete()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()