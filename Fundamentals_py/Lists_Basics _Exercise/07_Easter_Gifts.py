name_of_gifts = input().split()

list_gifts = name_of_gifts  # This should be a list of strings, not a list of lists

has_to_end = False
while True:
    inp_from_user = input().split()
    command = inp_from_user[0]

    if command == 'No Money':
        has_to_end = True
        break

    gft = inp_from_user[1]  # the gift name

    if command == 'OutOfStock':
        list_gifts = [gift if gift != gft else "None" for gift in list_gifts]

    elif command == 'Required':
        idx = int(inp_from_user[2])
        if 0 <= idx < len(list_gifts):  # Check if the index is valid
            list_gifts[idx] = gft

    elif command == "JustInCase":
        list_gifts[-1] = gft

final_gifts = [gift for gift in list_gifts if gift != "None"]

print(" ".join(final_gifts))
