from collections import deque

n = int(input())

pumps = deque()

for _ in range(n):
    values = input().split()
    fuel = int(values[0])
    distance = int(values[1])
    pumps.append((fuel,distance))

start = 0

while True:
    success = True
    capacity = 0
    for fuel,distance in pumps:
        capacity += fuel
        capacity -= distance
        if capacity < 0:
            success = False
            break


    if success:
        print(start)
        break

    start += 1
    pumps.rotate(-1)



