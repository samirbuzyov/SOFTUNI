from collections import deque

green_light_duration = int(input())
free_window_duration = int(input())

car_line = deque()
cars_count = 0

command = input()
while command != 'END':
    if command != 'green':
        car_line.append(command)
    else:
        green = green_light_duration
        full = green_light_duration + free_window_duration
        while green > 0 and car_line:
            car = car_line.popleft()
            car_time = len(car)
            if car_time <= green:
                green -= car_time
                full -= car_time
                cars_count += 1
            elif car_time <= full:
                green = 0
                full -= car_time
                cars_count += 1
            else:
                print("A crash happened!")
                print(f"{car} was hit at {car[full]}.")
                exit()
    command = input()

print("Everyone is safe.")
print(f"{cars_count} total cars passed the crossroads.")
