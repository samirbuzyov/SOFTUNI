width = int(input())
length = int(input())
height = int(input())

room_space = width * length * height
space_with_cartons = 0


command = input()

while command != 'Done':
    carton_count = int(command)
    space_with_cartons += carton_count

    if space_with_cartons >= room_space:
        break
    command = input()

free_space = room_space - space_with_cartons

if command == 'Done':
    print(f"{free_space} Cubic meters left.")
else:
    print(f"No more free space! You need {-free_space} Cubic meters more.")