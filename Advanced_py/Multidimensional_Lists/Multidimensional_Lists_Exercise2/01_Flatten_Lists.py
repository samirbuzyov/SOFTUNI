strings = input().split('|')

matrix = []

for idx in range(len(strings) - 1, -1, -1):
    row = strings[idx].split()
    if row:
        matrix.append(row)

for row in matrix:
    print(*row, end=' ')