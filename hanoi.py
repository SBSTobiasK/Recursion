loop = 0

def move(f, t):
    print("Move {} to {}.".format(f,t))

def hanoi(n, f, v, t):
    global loop
    if n==0:
        pass
    else:
        hanoi((n-1), f, t, v)
        move(f,t)
        loop += 1
        hanoi((n-1), v, f, t)

hanoi(7, "A","B","C")
print(loop)

#https://www.youtube.com/watch?v=8lhxIOAfDss
#https://www.youtube.com/watch?v=2SUvWfNJSsM