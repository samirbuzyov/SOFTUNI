from collections import deque

quantity_water = int(input())
queue = deque()
flag = False
while True:
    if flag:
        break
    command = input()

    if command == "Start":
        while True:
            receive = input().split()
            if receive[0] == 'End':
                print(f"{quantity_water} liters left")
                flag = True
                break
            elif len(receive) == 1:
                liters = int(receive[0])
                if liters <= quantity_water:
                    print(f"{queue.popleft()} got water")
                    quantity_water -= liters
                else:
                    print(f"{queue.popleft()} must wait")
            else:
                liters = int(receive[1])
                quantity_water += liters


    else:
        queue.append(command)

