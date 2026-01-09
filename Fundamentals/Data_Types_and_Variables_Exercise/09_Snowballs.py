n = int(input())

max_value = 0
max_weight = 0
max_time = 0
max_quality = 0
for i in range(n):
    weight = int(input())
    time_needed = int(input())
    quality = int(input())

    value = (weight / time_needed) ** quality

    if max_value < value:
        max_value = value
        max_weight = weight
        max_time = time_needed
        max_quality = quality

print(f'{max_weight} : {max_time} = {max_value:.0f} ({max_quality})')

