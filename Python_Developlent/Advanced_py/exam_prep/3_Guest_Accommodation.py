def accommodate(*guests, **rooms):
    sorted_rooms = sorted(rooms.items(),key=lambda x: (x[1], x[0]))
    accommodation = {}
    unsuccessful_accommodation = 0

    for guest in guests:
        for room in sorted_rooms:
            if room[1] >=guest:
                accommodation[room[0][-3:]] = guest
                sorted_rooms.remove(room)
                break
        else:
            unsuccessful_accommodation += guest
    result = ''
    if accommodation:
        result += f"A total of {len(accommodation)} accommodations were completed!\n"
        for room, guest in accommodation.items():
            result += f"Room {room} accommodates {guest} guests\n"
    else:
        result += "No accommodations were completed!\n"

    if unsuccessful_accommodation > 0:
        result += f"Guests with no accommodation: {unsuccessful_accommodation}\n"

    if sorted_rooms:
        result += f"Empty rooms: {len(sorted_rooms)}\n"

    return result

print(accommodate(5, 4, 2, room_305=6, room_410=5, room_204=2))
print(accommodate(10, 9, 8, room_307=6, room_802=5))
print(accommodate(1, 2, 4, 8, room_102=3, room_101=2, room_103=2))