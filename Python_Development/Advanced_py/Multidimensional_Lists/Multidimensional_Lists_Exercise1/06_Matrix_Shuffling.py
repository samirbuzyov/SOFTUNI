r, c = [int(x) for x in input().split()]

matrix = [[int(x) for x in input().split()] for _ in range(r)]

while True:
    command = input().split()
    if command[0] == "END":
        break

    if len(command) == 5 and command[0] == "swap":
        row1, col1, row2, col2 = map(int, command[1:])
        if 0 <= row1 < r and 0 <= col1 < c and 0 <= row2 < r and 0 <= col2 < c:
            matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
            for row in matrix:
                print(*row)
            continue

    print("Invalid input!")
