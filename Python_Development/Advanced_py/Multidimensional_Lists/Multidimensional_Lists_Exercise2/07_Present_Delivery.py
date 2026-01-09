m = int(input())
n = int(input())

directions = {
    "up":(-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

matrix = []
santa_r, santa_c = -1, -1
nice_kids = 0
nice_kids_presents = 0

for row in range(n):
    matrix.append(input().split())
    for col in range(n):
        if matrix[row][col] == 'S':
            santa_r, santa_c = row, col

        if matrix[row][col] == 'V':
            nice_kids += 1

while True:
    if m == 0:
        break
    command = input()
    if command == "Christmas morning":
        break

    dr, dc = directions[command]
    next_r, next_c = santa_r + dr, santa_c + dc
    if 0 <= next_r < n and 0 <= next_c < n:

        if matrix[next_r][next_c] == 'V':
            nice_kids_presents += 1
            nice_kids -= 1
            m -= 1
            matrix[santa_r][santa_c] = '-'
            matrix[next_r][next_c] = 'S'
            santa_r,santa_c = next_r,next_c

        elif matrix[next_r][next_c] == 'X' or  matrix[next_r][next_c] == '-':
            matrix[santa_r][santa_c] = '-'
            matrix[next_r][next_c] = 'S'
            santa_r, santa_c = next_r, next_c

        elif matrix[next_r][next_c] == 'C':
            for nr,nc in directions.values():
                nr += next_r
                nc += next_c
                if 0<=nr < n and 0<=nc < n:
                    if matrix[nr][nc] == 'V' or matrix[nr][nc] == 'X':
                        m -= 1
                        if matrix[nr][nc] == 'V':
                            nice_kids-= 1
                            nice_kids_presents += 1
                        matrix[nr][nc] = '-'
                matrix[santa_r][santa_c] = '-'
                matrix[next_r][next_c] = 'S'
                santa_r, santa_c = next_r, next_c



if m == 0 and nice_kids > 0:
    print("Santa ran out of presents!")

[print(*row) for row in matrix]

if nice_kids == 0:
    print(f"Good job, Santa! {nice_kids_presents} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids} nice kid/s.")