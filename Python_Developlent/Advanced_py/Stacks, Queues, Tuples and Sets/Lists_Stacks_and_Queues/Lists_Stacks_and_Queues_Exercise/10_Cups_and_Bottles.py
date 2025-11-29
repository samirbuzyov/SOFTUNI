from collections import deque

cups = deque([int(el) for el in input().split()])
bottles = [int(el) for el in input().split()]

wasted_water = 0
cup = cups[0]
while cups:
    if not bottles:
        break

    bottle = bottles.pop()


    cup -= bottle
    if cup <= 0:
        wasted_water -= cup
        cups.popleft()
        if not cups:
            break
        cup = cups[0]

if not cups:
    print(f'Bottles:',*bottles, sep=' ')

if not bottles:
    print(f'Cups:',*cups, sep=' ')

print(f"Wasted litters of water: {wasted_water}")




