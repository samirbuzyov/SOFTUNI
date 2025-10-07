field_size = int(input())
bunny_r, bunny_c = 0,0

matrix = []
for row in range(field_size):
    matrix.append(input().split())
    for col in range(field_size):
        cell = matrix[row][col]
        if cell == 'B':
            bunny_r, bunny_c = row, col

directions = {"up":(-1,0), 'down' : (1,0),'left' : (0,-1), 'right' : (0,1)}
max_eggs = float("-inf")
max_direction = ''
max_eggs_matrix = []

for direction, move in directions.items():
    eggs = 0
    curr_egg_matrix = []
    next_r = bunny_r + move[0]
    next_c = bunny_c + move[1]

    while 0<=next_r < field_size and 0<=next_c < field_size:
        if matrix[next_r][next_c] == 'X':
            break
        eggs += int(matrix[next_r][next_c])
        curr_egg_matrix.append([next_r,next_c])
        next_r+= move[0]
        next_c += move[1]

    if eggs > max_eggs and curr_egg_matrix:
        max_eggs = eggs
        max_eggs_matrix = curr_egg_matrix
        max_direction = direction

print(max_direction)
[print(row) for row in max_eggs_matrix]
print(max_eggs)