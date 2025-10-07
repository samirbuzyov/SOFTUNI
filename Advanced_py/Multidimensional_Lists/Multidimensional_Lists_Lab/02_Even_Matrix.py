rows = int(input())
matrix = [[int(el) for el in input().split(', ') if int(el) % 2 == 0] for _ in range(rows)]
# for _ in range(rows):
#     row_data = [int(el) for el in input().split(', ') if int(el) %2 == 0]
#     matrix.append(row_data)


for row_index in range(len(matrix)):
    for col_index in range(len(matrix[row_index])):
        print(matrix[row_index][col_index], end=', ')