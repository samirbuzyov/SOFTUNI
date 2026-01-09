# rows, cols = [int(x) for x in input().split()]
#
# matrix = [[int(el) for el in input().split()] for _ in range(rows)]
#
# result = []
# max_sum = float('-inf')
#
# for row in range(rows - 2):
#     for col in range(cols - 2):
#         current_sum = (
#             matrix[row][col] + matrix[row][col + 1] + matrix[row][col + 2] +
#             matrix[row + 1][col]+ matrix[row + 1][col + 1]+ matrix[row + 1][col + 2] +
#             matrix[row + 2][col]+ matrix[row + 2][col + 1]+ matrix[row + 2][col + 2])
#
#         if current_sum > max_sum:
#             max_sum = current_sum
#             result = [
#                 [matrix[row][col], matrix[row][col + 1], matrix[row][col + 2]],
#                 [matrix[row + 1][col], matrix[row + 1][col + 1], matrix[row + 1][col + 2]],
#                 [matrix[row + 2][col], matrix[row + 2][col + 1], matrix[row + 2][col + 2]]
#
#             ]
# print(f'Sum = {max_sum}')
# for row in result:
#     print(' '.join(str(x) for x in row))

rows, cols = [int(x) for x in input().split()]

matrix = [[int(el) for el in input().split()] for _ in range(rows)]

max_sum = float('-inf')
max_row = -1
max_col = -1
for row in range(rows - 2):
    for col in range(cols - 2):
        current_sum = 0
        for r in range(row, row + 3):
            for c in range(col, col + 3):
                current_sum += matrix[r][c]


        if current_sum > max_sum:
            max_sum = current_sum
            max_row = row
            max_col = col

print(f'Sum = {max_sum}')

max_submatrix = [matrix[r][max_col:max_col+3] for r in range(max_row,max_row + 3)]
[print(*row) for row in max_submatrix]