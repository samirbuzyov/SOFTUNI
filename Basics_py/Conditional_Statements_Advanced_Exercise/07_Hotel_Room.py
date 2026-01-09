month = input()
nights = int(input())


apartment_per_night = 0
studio_per_night = 0
discount_studio = 0
discount_apartment = 0
if month == 'May' or month == 'October':
    apartment_per_night = 65
    studio_per_night = 50
    if nights > 14:
        discount_studio = 0.30
    elif nights > 7:
        discount_studio = 0.05
    else:
        discount_studio = 0
elif month == 'June' or month == 'September':
    studio_per_night =75.20
    apartment_per_night = 68.70
    if nights > 14:
        discount_studio = 0.2

elif month == 'July' or month == 'August':
    studio_per_night =76
    apartment_per_night = 77

if nights > 14:
    discount_apartment = 0.10

total_apartment = (1-discount_apartment) * apartment_per_night * nights
total_studio = (1 - discount_studio) * studio_per_night * nights


print(f'Apartment: {total_apartment:.2f} lv.')
print(f'Studio: {total_studio:.2f} lv.')




