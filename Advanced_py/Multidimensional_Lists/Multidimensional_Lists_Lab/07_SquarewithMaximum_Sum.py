rows, cols = [int(x) for x in input().split(', ')]

matrix = [[int(el) for el in input().split(', ')] for _ in range(rows)]

max_sum = float('-inf')
best_submatrix = []

for row in range(rows - 1):
    for col in range(cols - 1):
        current_sum = (
            matrix[row][col] + matrix[row][col + 1] +
            matrix[row + 1][col] + matrix[row + 1][col + 1]
        )
        if current_sum > max_sum:
            max_sum = current_sum
            best_submatrix = [
                [matrix[row][col], matrix[row][col + 1]],
                [matrix[row + 1][col], matrix[row + 1][col + 1]]
            ]

for row in best_submatrix:
    print(' '.join(str(x) for x in row))
print(max_sum)
