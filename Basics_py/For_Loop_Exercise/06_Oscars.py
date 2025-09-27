# actor_name = input()
# starting_points = float(input())
# number_raters = int(input())
#
# points = 0
# final_points = 0
# for rater in range(number_raters):
#     name_rater = input()
#     points_rater = float(input())
#     total_points_rater = len(name_rater) * (points_rater / 2)
#     points += total_points_rater
#     final_points = points + starting_points
#
#     if final_points >= 1250.5:
#         print(f'Congratulations, {actor_name} got a nominee for leading role with {round(final_points, 1)}!')
#         break
#     else:
#         continue
#
# if final_points < 1250.5:
#     needed_points = 1250.5 - final_points
#     print(f'Sorry, {actor_name} you need {needed_points} more!')


actor_name = input()  # Input the actor's name
starting_points = float(input())  # Input starting points
number_raters = int(input())  # Input the number of raters

points = 0
final_points = 0
# Loop through all the raters
for rater in range(number_raters):
    name_rater = input()  # Input rater's name
    points_rater = float(input())  # Input the points the rater gives
    total_points_rater = len(name_rater) * (points_rater / 2)  # Calculate rater's contribution
    points += total_points_rater  # Add to total points
    final_points = starting_points + points
    if final_points >= 1250.5:
        print(f'Congratulations, {actor_name} got a nominee for leading role with {final_points:.1f}!')
        break
    else:
        continue

if final_points < 1250.5:
    needed_points = 1250.5 - final_points
    print(f'Sorry, {actor_name} you need {needed_points:.1f} more!')
