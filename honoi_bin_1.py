count=0
def move_disk(x):
    global count
    count +=1
    print(x)


def solve_toh(n_disks):
    if n_disks == 0:
        return
    solve_toh(n_disks-1)
    move_disk(n_disks-1)
    solve_toh(n_disks-1)

solve_toh(5)
print("\t", count)