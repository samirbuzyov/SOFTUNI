n = int(input())
for i in range(n):
    string = input()
    is_pure = False

    for char in string:
        if char == ',':
            is_pure =True
        elif char == '_':
            is_pure = True
        elif char == '.':
            is_pure = True


    if is_pure:
        print(f'{string} is not pure!')
    else:
        print(f"{string} is pure.")
