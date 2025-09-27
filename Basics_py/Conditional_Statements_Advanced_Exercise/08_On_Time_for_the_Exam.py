exam_hour = int(input())
exam_minute = int(input())
arrive_hour = int(input())
arrive_minute = int(input())

exam_time_in_minutes = exam_hour * 60 + exam_minute
arrive_time_in_minutes = arrive_hour * 60 + arrive_minute

time_diff = arrive_time_in_minutes - exam_time_in_minutes

if time_diff > 0:
    print("Late")
    hours = time_diff // 60
    minutes = time_diff % 60
    if hours > 0:
        print(f"{hours}:{minutes:02d} hours after the start")
    else:
        print(f"{minutes} minutes after the start")
elif time_diff >= -30:
    time_diff = exam_time_in_minutes - arrive_time_in_minutes
    print("On time")
    minutes = time_diff % 60
    if time_diff == 0:
        pass
    else:
        print(f'{minutes} minutes before the start')

elif time_diff > -60:
    print("Early")
    minutes = -time_diff
    print(f"{minutes} minutes before the start")

else:

    print("Early")
    minutes = -time_diff
    hours = minutes // 60
    minutes = minutes % 60
    print(f"{hours}:{minutes:02d} hours before the start")
