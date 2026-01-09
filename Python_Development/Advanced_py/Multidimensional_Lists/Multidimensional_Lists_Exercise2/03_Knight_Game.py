n = int(input())

matrix = [[el for el in input()] for _ in range(n)]
knights = []
for row in range(n):
    for col in range(n):
        if matrix[row][col] == 'K':
            knights.append([row, col])

possible_moves = [(-1,-2), (-2,-1), (-2,1), (-1,2),(1,-2),(2,-1), (1,2),(2,1)]

removed_knights = 0

while True:
    max_hits = 0
    max_knight = [0,0]

    for k_row,k_col in knights:
        hits = 0
        for move_r, move_c in possible_moves:
            next_r, next_c = k_row + move_r, k_col + move_c
            if 0<=next_r < n and 0<=next_c <n:
                if matrix[next_r][next_c] == 'K':
                    hits += 1

        if hits>max_hits:
            max_hits = hits
            max_knight = [k_row, k_col]

    if max_hits > 0:
        knights.remove(max_knight)
        matrix[max_knight[0]][max_knight[1]] = '0'
        removed_knights += 1
    else:
        break
print(removed_knights)