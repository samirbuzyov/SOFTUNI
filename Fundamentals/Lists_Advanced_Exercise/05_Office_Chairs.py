rooms = int(input())

chairs_count = 0
visitors_count = 0


for room in range(1, rooms+ 1):
    chair_visitor = input().split(' ')
    chairs = chair_visitor[0]
    visitors = int(chair_visitor[1])
    visitors_count += visitors
    chairs_room = 0
    for letter in chairs:
        if letter == 'X':
            chairs_count += 1
            chairs_room += 1

    if chairs_room < visitors:
        print(f"{visitors - chairs_room} more chairs needed in room {room}")

if visitors_count <= chairs_count:
    print(f"Game On, {chairs_count - visitors_count} free chairs left")