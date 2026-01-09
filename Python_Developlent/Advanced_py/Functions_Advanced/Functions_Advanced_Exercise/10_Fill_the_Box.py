from collections import deque

def fill_the_box(*args):
    box = 1
    free = 0
    cubes = deque(args)
    for _ in range(3):
        temp = cubes.popleft()
        box *= temp

    while True:
        if cubes[0] == 'Finish':
            break
        cube = int(cubes.popleft())
        temp = box - cube
        if temp > 0:
            box-= cube
        else:
            box = 0
            free -=temp

    if box >0:
        return f"There is free space in the box. You could put {box} more cubes."
    else:
        return f"No more free space! You have {free} more cubes."



print(fill_the_box(5, 5,2, 40, 11, 7, 3, 1, 5,"Finish"))
print(fill_the_box(2, 8,

2, 2, 1, 7, 3, 1, 5,

"Finish"))