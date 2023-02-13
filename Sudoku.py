import numpy as np

grid1 = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]]

grid = [[9, 2, 4, 1, 5, 6, 3, 0, 8], [0, 0, 3, 8, 7, 9, 0, 2, 1], [5, 0, 8, 3, 0, 4, 6, 9, 0], [4, 1, 6, 0, 0, 3, 8, 0, 9], [0, 9, 0, 7, 8, 0, 5, 4, 3], [8, 3, 5, 2, 9, 0, 0, 7, 6], [6, 4, 0, 5, 2, 8, 1, 0, 7], [0, 5, 1, 6, 3, 0, 4, 8, 2], [7, 8, 2, 0, 4, 1, 9, 3, 0]]

def possible(y,x,n):
    global grid
    for i in range(0,9):
        if grid[y][i] == n:
            return False
    for i in range(0,9):
        if grid[i][x] == n:
            return False
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if grid[y0+i][x0+j] == n:
                return False
    return True
def solve():
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1,10):
                    if possible(y,x,n):
                        grid[y][x] = n
                        solve()
                        grid[y][x] = 0
                return
    print(np.matrix(grid))
    input("More?")

solve()