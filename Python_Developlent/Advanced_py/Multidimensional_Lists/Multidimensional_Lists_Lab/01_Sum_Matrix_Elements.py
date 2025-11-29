row, columns = [int(el) for el in input().split(', ')]
suma = 0
matrix = []
for _ in range(row):
    row_data = [int(el) for el in input().split(', ')]
    suma += sum(row_data)
    matrix.append(row_data)

print(suma)
print(matrix)