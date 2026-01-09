from math import floor
tournaments = int(input())
starting_points = int(input())


won_tournaments = 0
tournament_points = 0
for _ in range(tournaments):
    stage_of_tour = input()
    if stage_of_tour == 'W':
        tournament_points += 2000
        won_tournaments += 1
    elif stage_of_tour == 'F':
        tournament_points += 1200
    elif stage_of_tour == 'SF':
        tournament_points += 720

total_points = starting_points + tournament_points
print(f'Final points: {total_points}')

average_points = tournament_points / tournaments
print(f'Average points: {floor(average_points)}')

won_tournaments_percent = won_tournaments / tournaments * 100
print(f'{won_tournaments_percent:.2f}%')