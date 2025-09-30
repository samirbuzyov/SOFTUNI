capacity = 255
tank = 0

n = int(input())

for i in range(n):
    liters = int(input())
    tank += liters
    if tank > capacity:
        print('Insufficient capacity!')
        tank -= liters

    else:
        continue

print(tank)