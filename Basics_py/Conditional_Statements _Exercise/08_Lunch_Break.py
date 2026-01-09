from math import ceil

series_name = input()
episode = int(input())
breakk = int(input())

lunch_time = 1/8 * breakk
rest = 1/4 * breakk
free_break_time = breakk - lunch_time - rest

if episode <= free_break_time:
    left_time_1 = free_break_time - episode
    left_time = ceil(left_time_1)
    print(f'You have enough time to watch {series_name} and left with {left_time} minutes free time.')
else:
    needed_time_1 = episode - free_break_time
    needed_time = ceil(needed_time_1) 
    print(f"You don't have enough time to watch {series_name}, you need {needed_time} more minutes.")
