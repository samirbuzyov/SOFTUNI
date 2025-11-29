from collections import deque
n, m = [int(el) for el in input().split()]
snake_string = deque(input())

matrix = []

for row in range(n):
    matrix.append([''] * m)
    for col in range(m):
        if row % 2 == 0:
            matrix[row][col] = snake_string[0]
        else:
            matrix[row][-col - 1] = snake_string[0]
        snake_string.rotate(-1)

[print(*row, sep='') for row in matrix]