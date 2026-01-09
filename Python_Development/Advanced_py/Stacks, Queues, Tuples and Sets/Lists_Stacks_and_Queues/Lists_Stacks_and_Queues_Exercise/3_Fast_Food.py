from collections import deque

quantity_food = int(input())

orders = input().split()

queue = deque([int(x) for x in orders])

print(max(queue))
flag = True
while queue:

    if quantity_food - queue[0]< 0:
        flag = False
        break

    quantity_food -= queue.popleft()

if flag:
    print("Orders complete")
else:
    print("Orders left: ", end='')
    while queue:
        print(queue.popleft(), end=' ')