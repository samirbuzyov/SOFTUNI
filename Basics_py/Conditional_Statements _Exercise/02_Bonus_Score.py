# starting_points = int(input())
# bonus_points = 0


# if starting_points <= 100:
#     bonus_points += 5
#     if starting_points % 2 == 0:
#         bonus_points += 1
#     elif starting_points % 10 == 5:
#         bonus_points += 2
    
# elif 1000 >= starting_points > 100:
#     bonus_points += 20/100 * starting_points
#     if starting_points % 2 == 0:
#         bonus_points += 1
#     elif starting_points % 10 == 5:
#         bonus_points += 2

# else:
#     bonus_points += 10/100 * starting_points
#     if starting_points % 2 == 0:
#         bonus_points += 1
#     elif starting_points % 10 == 5:
#         bonus_points += 2

# print(bonus_points)
# print(starting_points + bonus_points)



starting_points = int(input())
bonus_points = 0
if starting_points <= 100:
    bonus_points += 5
elif 1000 >= starting_points > 100:
     bonus_points += 20/100 * starting_points
else:
     bonus_points += 10/100 * starting_points

additional_bonus_points = 0

if starting_points % 2 == 0:
     additional_bonus_points += 1
elif starting_points % 10 == 5:
     additional_bonus_points += 2

total_bonus = bonus_points + additional_bonus_points
total = total_bonus + starting_points

print(total_bonus)
print(total)

