from collections import deque

bullet_price = int(input())
gun_barrel_size = int(input())
bullets = [int(el) for el in input().split()]
locks = deque([int(el) for el in input().split()])
intelligence_value = int(input())

barrel = gun_barrel_size
while bullets:
    if barrel == 0:
        print('Reloading!')
        barrel = gun_barrel_size
    if not locks:
        break


    bullet = bullets.pop()
    if bullet <= locks[0]:
        locks.popleft()
        print('Bang!')
    else:
        print('Ping!')
    barrel -=1
    intelligence_value -= bullet_price



if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    print(f"{len(bullets)} bullets left. Earned ${intelligence_value}")
