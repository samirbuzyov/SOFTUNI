n = int(input())

matrix = [[int(el) for el in input().split()] for _ in range(n)]
total = 0

for idx in range(n):
    total += matrix[idx][idx]

print(total)