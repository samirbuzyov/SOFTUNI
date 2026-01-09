# floors = int(input())
# rooms = int(input())
#
# for floor in range(floors, 0, -1):
#     for room in range(rooms):
#         if floor == floors:
#             print(f'L{floor}{room}', end=" ")
#         elif floor % 2 == 0:
#             print(f'O{floor}{room}',end=" ")
#         else:
#             print(f'А{floor}{room}',end=" ")
#     print()

total_floors = int(input())
rooms_per_floor = int(input())
for floor in range(total_floors, 0, -1):
    for room in range (rooms_per_floor):
        if floor == total_floors:
            print("L{0}{1} ".format(floor,room), end="")
        elif floor % 2 == 0:
            print("O{0}{1} ".format(floor,room), end="")
        elif floor % 2 != 0:
            print("A{0}{1} ".format(floor,room), end="")
    print('')

