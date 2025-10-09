n = int(input())
field = [[el for el in input().split()] for _ in range(n)]

move = {
    'up' : (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

player_row, player_col = -1, -1
for i in range(len(field)):
    for j in range(len(field[i])):
        if field[i][j] == 'P':
            player_row,player_col = i, j


stars = 2

while 0 < stars < 10:
    command = input()
    r, c = move[command]
    if  0 <= player_row + r < n and 0 <= player_col + c < n:
        current_row = player_row + r
        current_col = player_col + c

        if field[current_row][current_col] == '*':
            stars += 1
            field[player_row][player_col] = '.'
            player_row, player_col = current_row, current_col

        elif field[current_row][current_col] == '#':
            stars -= 1
        else:
            field[player_row][player_col] = '.'
            player_row, player_col = current_row, current_col


        field[player_row][player_col] = 'P'

    else:
        player_row,player_col = 0, 0

if stars == 10:
    print("You won! You have collected 10 stars.")
else:
    print("Game over! You are out of any stars.")

print(f"Your final position is [{player_row}, {player_col}]")
for row in field:
    print(' '.join(row))