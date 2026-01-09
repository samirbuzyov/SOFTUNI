vacation = float(input())
puzzles = int(input())
puzzles_price = puzzles * 2.60
doll = int(input())
doll_price = doll * 3
bear = int(input())
bear_price = bear * 4.1
minion = int(input())
minion_price = minion *8.2
car = int(input())
car_price = car * 2
number_of_toys = puzzles + car + bear + doll + minion


total_toys = puzzles_price + car_price + bear_price + doll_price + minion_price

if number_of_toys >= 50:
    discount = 0.25 * total_toys
    total_toys -= discount

total = 0.9 * total_toys


if total >= vacation:
    money_left = total - vacation
    print(f'Yes! {money_left:.2f} lv left.')

else:
    money_notenough = vacation - total
    print(f'Not enough money! {money_notenough:.2f} lv needed.')