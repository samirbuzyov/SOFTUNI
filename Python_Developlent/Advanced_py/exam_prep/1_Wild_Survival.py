from collections import deque
beehive = deque(int(el) for el in input().split())
bee_eaters_hive = [int(el) for el in input().split()]

bea_eater_kill = 7

while beehive and bee_eaters_hive:
    bee_group = beehive.popleft()
    bee_eaters_group = bee_eaters_hive.pop()

    while bee_group > 0 and bee_eaters_group > 0:
        bee_group -= bea_eater_kill
        if bee_group >= 0:
            bee_eaters_group -= 1

    if bee_eaters_group > 0:
        bee_eaters_hive.append(bee_eaters_group)

    if bee_group > 0:
        beehive.append(bee_group)

print("The final battle is over!")

if beehive:
    print(f"Bee groups left: {", ".join(str(el) for el in beehive)}")
elif bee_eaters_hive:
    print(f"Bee-eater groups left: {", ".join(str(el) for el in bee_eaters_hive)}")
else:
    print("But no one made it out alive!")