from collections import deque

n, m = [int(x) for x in input().split()]
matrix = [list(input()) for _ in range(n)]
commands = deque(input())

directions = {
    'L': (0, -1),
    'R': (0, 1),
    'U': (-1, 0),
    'D': (1, 0)
}

bunnies = deque()
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 'P':
            p_row, p_col = i, j
        elif matrix[i][j] == 'B':
            bunnies.append((i, j))

won = False
dead = False

while commands:
    command = commands.popleft()

    dr, dc = directions[command]
    next_r, next_c = p_row + dr, p_col + dc

    matrix[p_row][p_col] = '.'

    if 0 <= next_r < n and 0 <= next_c < m:
        if matrix[next_r][next_c] == 'B':
            dead = True
        else:
            matrix[next_r][next_c] = 'P'
        p_row, p_col = next_r, next_c
    else:
        won = True

    new_bunnies = deque()
    while bunnies:
        br, bc = bunnies.popleft()
        for dr, dc in directions.values():
            nr, nc = br + dr, bc + dc
            if 0 <= nr < n and 0 <= nc < m:
                if matrix[nr][nc] == 'P':
                    dead = True
                if matrix[nr][nc] != 'B':
                    matrix[nr][nc] = 'B'
                    new_bunnies.append((nr, nc))
    bunnies = new_bunnies

    if won or dead:
        break

# Final output
for row in matrix:
    print(''.join(row))
if won:
    print(f'won: {p_row} {p_col}')
elif dead:
    print(f'dead: {p_row} {p_col}')
