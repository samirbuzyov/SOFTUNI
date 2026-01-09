budget = int(input())
season = input()
num_fishers = int(input())


boat_rent = 0
discount = 0

if season == 'Spring':
    boat_rent = 3000

elif season == 'Summer' or season == 'Autumn':
    boat_rent = 4200

elif season == 'Winter':
    boat_rent = 2600


if num_fishers <= 6:
    discount = 0.1
elif 7 <= num_fishers <= 11:
    discount = 0.15
elif num_fishers >= 12:
    discount = 0.25

extra_discount = 0.0
if num_fishers % 2 ==0 and season != 'Autumn':
    extra_discount = 0.05



total_price = (1-discount) * ( 1 - extra_discount) * boat_rent
if budget >= total_price:
    money_left = budget - total_price
    print(f"Yes! You have {money_left:.2f} leva left.")


elif total_price > budget:
    money_needed = total_price - budget
    print(f"Not enough money! You need {money_needed:.2f} leva.")
