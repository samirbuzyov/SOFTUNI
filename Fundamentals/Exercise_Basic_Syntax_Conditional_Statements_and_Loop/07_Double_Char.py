command = ''


while True:
    command = input()
    new_string = ''
    if command == 'End':
        break
    elif command == 'SoftUni':
        continue

    for char in command:
        new_string += 2* char

    print(new_string)
