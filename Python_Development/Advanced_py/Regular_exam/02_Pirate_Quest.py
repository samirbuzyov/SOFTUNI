n =int(input())

sea = [[el for el in input()] for _ in range(n)]

durability = 100
treasure_count = 0
one_time_restore = False

move = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}
player_row, player_col = 0, 0
for i in range(n):
    for j in range(n):
        if sea[i][j] == "S":
            player_row,player_col = i, j

        elif sea[i][j] == "*":
            treasure_count += 1


while durability > 0 and treasure_count > 0:
    command = input()
    if command == 'stop':
        break

    r, c = move[command]
    next_r,next_c = player_row + r, player_col + c

    if next_r == n:
        next_r = 0
    elif next_r == -1:
        next_r = n-1
    if next_c == n:
        next_c= 0
    elif next_c == -1:
        next_c = n-1

    if sea[next_r][next_c] == '*':
        treasure_count-=1
        sea[player_row][player_col] = '.'
        player_row,player_col = next_r,next_c
    elif sea[next_r][next_c] == 'C':
        sea[player_row][player_col] = '.'
        if not one_time_restore:
            one_time_restore = True
            durability += 25
            if durability > 100:
                durability = 100
    elif sea[next_r][next_c] == 'M':
        durability -= 25
        sea[player_row][player_col] = '.'
    else:
        sea[player_row][player_col] = '.'

    player_row,player_col = next_r, next_c
    sea[player_row][player_col] = 'S'

if durability == 0:
    print(f"Shipwreck! Last known coordinates ({player_row}, {player_col})")

if treasure_count == 0:
    print("Yo-ho-ho! All treasure chests collected!")

if command == 'stop':
    print("Retreat! Some treasures remain unclaimed.")

print(f"Ship Durability: {durability}")
if treasure_count > 0:
    print(f"Unclaimed chests: {treasure_count}")

for row in sea:
    print(''.join(row))