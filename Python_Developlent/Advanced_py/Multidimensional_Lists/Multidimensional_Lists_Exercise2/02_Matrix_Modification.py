rows = int(input())

matrix = [[int(x) for x in input().split()]for _ in range(rows)]

while True:
    command = input().split()
    operation = command[0]
    if operation == 'END':
        break

    c_row = int(command[1])
    c_col =int(command[2])
    value = int(command[3])
    if 0<=c_row< rows and 0<=c_col< rows:
        if operation == "Add":
            matrix[c_row][c_col] += value
        elif operation == 'Subtract':
            matrix[c_row][c_col] -= value

    else:
        print("Invalid coordinates")

[print(*row) for row in matrix]