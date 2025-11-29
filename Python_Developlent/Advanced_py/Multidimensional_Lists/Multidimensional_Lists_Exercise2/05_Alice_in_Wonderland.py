n = int(input())
matrix = [[el for el in input().split()] for _ in range(n)]

directions = {
    "up":(-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

alice_r, alice_c = 0 ,0
rhole_r, rhole_c = 0, 0

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 'R':
            rhole_r, rhole_c = i, j
        if matrix[i][j] == 'A':
            alice_r, alice_c = i, j

tea_collected = 0
not_in_territory = False

while True:
    if not_in_territory:
        break
    if tea_collected >= 10:
        break

    command = input()

    dr, dc = directions[command]
    matrix[alice_r][alice_c] = '*'
    next_r, next_c = alice_r + dr, alice_c + dc

    if 0<=next_r < n and 0<=next_c < n:
        if matrix[next_r][next_c] == 'R':
            matrix[next_r][next_c] = '*'
            not_in_territory = True
        elif matrix[next_r][next_c].isdigit():
            tea_collected+= int(matrix[next_r][next_c])
            matrix[next_r][next_c] = 'A'
            alice_r, alice_c = next_r, next_c
        else:
            matrix[next_r][next_c] = 'A'
            alice_r, alice_c = next_r, next_c
    else:
        not_in_territory = True
matrix[alice_r][alice_c] = '*'
if not_in_territory:
    print("Alice didn't make it to the tea party.")

if tea_collected >= 10:
    print("She did it! She went to the party.")

[print(*row) for row in matrix]