import numpy as np
import random

grid0 = [[0 for _ in range(9)] for _ in range(9)]
counter = 0
given = 25
def possible(y,x,n):
    global grid0
    for i in range(0,9):
        if grid0[y][i] == n:
            return False
    for i in range(0,9):
        if grid0[i][x] == n:
            return False
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if grid0[y0+i][x0+j] == n:
                return False
    return True
def fillgrid(given):
    global grid0
    if given < 1:
        pass
    else:
        while True:
            y = random.randint(0, 8)
            x = random.randint(0, 8)
            n = random.randint(1, 9)
            if grid0[y][x] == 0 and possible(y,x,n):
                break
        grid0[y][x] = n
        fillgrid(given-1)


fillgrid(given)
print(np.matrix(grid0))
print(grid0)

#for j in range(len(grid0)):
#    for k in range(len(grid0[j])):
#        if grid0[j][k] != 0:
#            counter += 1
#print(counter)





