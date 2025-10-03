receive = input()

while True:
    inpt = input().split()

    if inpt[0] == 'End':
        break

    command = inpt[0]

    if command == 'Translate':
        char = inpt[1]
        replacement = inpt[2]
        receive = receive.replace(char, replacement)
        print(receive)

    elif command == 'Includes':
        substring = inpt[1]
        print(substring in receive)

    elif command == 'Start':
        substring = inpt[1]
        print(receive.startswith(substring))

    elif command == 'Lowercase':
        receive = receive.lower()
        print(receive)

    elif command == "FindIndex":
        char = inpt[1]
        print(receive.rfind(char))

    elif command == 'Remove':
        startIndex = int(inpt[1])
        count1 = int(inpt[2])
        receive = receive[:startIndex] + receive[startIndex + count1:]
        print(receive)
