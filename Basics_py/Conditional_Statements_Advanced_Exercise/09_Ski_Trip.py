room_for_one_person = 18.00
apartment = 25.00
president_apartment = 35.00

days = int(input())
nights = days - 1
choice = input()
ocenka = input()

discount = 0
tip_no_tip = 0
per_night = 0

if choice == 'room for one person':
    per_night = room_for_one_person
elif choice == 'apartment':
    per_night = apartment
elif choice == 'president apartment':
    per_night = president_apartment


if nights < 10:
    if choice == 'room for one person':
        discount = 0
    elif choice == 'apartment':
        discount = 0.3
    elif choice == 'president apartment':
        discount = 0.1
    else:
        print('error')

elif 10 <= nights <= 15:
    if choice == 'room for one person':
        discount = 0
    elif choice == 'apartment':
        discount = 0.35
    elif choice == 'president apartment':
        discount = 0.15
    else:
        print('error')


elif nights > 15:
    if choice == 'room for one person':
        discount = 0
    elif choice == 'apartment':
        discount = 0.5
    elif choice == 'president apartment':
        discount = 0.2
    else:
        print('error')



if ocenka == 'positive':
    tip_no_tip = 0.25
elif ocenka == 'negative':
    tip_no_tip = -0.1
else:
    print('error')

price = nights * per_night
total_price = price * (1 - discount) * (1 + tip_no_tip)

print(f'{total_price:.2f}')

