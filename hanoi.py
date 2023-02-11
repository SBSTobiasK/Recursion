def move(f, t):
    print("Move {} to {}.".format(f,t))

def hanoi(n, f, v, t):
    if n==0:
        pass
    else:
        hanoi((n-1), f, t, v)
        move(f,t)
        hanoi((n-1), v, f, t)

hanoi(2, "A","B","C")

#https://www.youtube.com/watch?v=8lhxIOAfDss