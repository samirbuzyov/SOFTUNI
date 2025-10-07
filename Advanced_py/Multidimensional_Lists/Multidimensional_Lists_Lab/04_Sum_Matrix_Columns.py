rows, col = [int(x) for x in input().split(', ')]

matrix = [[int(el) for el in input().split()] for _ in range(rows)]

result = []

for col_idx in range(col):
    col_sum = 0
    for rows_idx in range(rows):
        col_sum+=matrix[rows_idx][col_idx]
    result.append(col_sum)

print(*result, sep='\n')