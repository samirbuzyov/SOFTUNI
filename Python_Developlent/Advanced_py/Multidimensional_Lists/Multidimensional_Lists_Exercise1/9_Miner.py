from collections import deque

n = int(input())
commands = deque(input().split())
matrix = [[el for el in input().split()] for _ in range(n)]

directions = {
    "left": (0, -1),
    "right": (0, 1),
    "up": (-1, 0),
    "down": (1, 0)
}

total_coal = 0
miner_r, miner_c = 0, 0

for row in range(n):
    for col in range(n):
        if matrix[row][col] == 's':
            miner_r, miner_c = row, col
        elif matrix[row][col] == 'c':
            total_coal += 1

coal_collected = 0

while commands:
    command = commands.popleft()
    dr, dc = directions[command]
    next_r = miner_r + dr
    next_c = miner_c + dc

    if 0 <= next_r < n and 0 <= next_c < n:
        cell = matrix[next_r][next_c]

        if cell == 'c':
            coal_collected += 1
            matrix[next_r][next_c] = 's'
            matrix[miner_r][miner_c] = '*'
            miner_r, miner_c = next_r, next_c
            if coal_collected == total_coal:
                print(f"You collected all coal! ({miner_r}, {miner_c})")
                break

        elif cell == 'e':
            print(f"Game over! ({next_r}, {next_c})")
            break

        else:
            matrix[next_r][next_c] = 's'
            matrix[miner_r][miner_c] = '*'
            miner_r, miner_c = next_r, next_c
else:
    remaining = total_coal - coal_collected
    print(f"{remaining} pieces of coal left. ({miner_r}, {miner_c})")
