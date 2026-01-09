# hours = int(input())
# minutes = int(input())

# total_minutes = minutes + 15

# total_hours = hours

# if total_minutes > 59:
#     hours += total_minutes // 60
#     total_minutes = total_minutes - 60
# elif total_minutes < 60:
#     total_hours = hours
#     total_minutes = total_minutes


# if hours > 23:
#     total_hours = hours - 24
# elif hours < 24:
#     total_hours = hours
#     total_minutes = total_minutes



# if total_minutes <=9:
#     print(f'{total_hours}:0{total_minutes}')
# else:
#     print(f'{total_hours}:{total_minutes}')

hours = int(input())
minutes = int(input()) 
minutes_plus_15 = minutes + 15

if minutes_plus_15 > 59:
    minutes_plus_15 -= 60
    hours += 1

if hours > 23:
    hours = 0

if minutes_plus_15 < 10:
    print(f'{hours}:{minutes_plus_15:02d}')
else: 
    print(f'{hours}:{minutes_plus_15}')

