count_numbers = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
for i in range(count_numbers):
    number = int(input())

    if number < 200:
        p1 += 1
    elif 200 <= number < 400:
        p2 += 1
    elif 400 <= number < 600:
        p3 += 1
    elif 600 <= number < 800:
        p4 += 1
    elif number >= 800:
        p5 += 1
p1_percent = (round(p1 / count_numbers * 100, 2))
p2_percent = (round(p2 / count_numbers * 100, 2))
p3_percent = (round(p3 / count_numbers * 100, 2))
p4_percent = (round(p4 / count_numbers * 100, 2))
p5_percent = (round(p5 / count_numbers * 100, 2))

print(f'{p1_percent:.2f}%')
print(f'{p2_percent:.2f}%')
print(f'{p3_percent:.2f}%')
print(f'{p4_percent:.2f}%')
print(f'{p5_percent:.2f}%')
