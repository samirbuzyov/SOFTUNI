record = float(input())
meters = float(input())
meters_per_second = float(input())


ivan_time = meters * meters_per_second


resistance = (meters // 15) * 12.5


total_ivan_time = ivan_time + resistance

if total_ivan_time < record:
    print(f'Yes, he succeeded! The new world record is {total_ivan_time:.2f} seconds.')
else:
    needed_time = total_ivan_time - record
    print(f'No, he failed! He was {needed_time:.2f} seconds slower.')