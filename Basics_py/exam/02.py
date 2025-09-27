from  math import ceil

name = input()
budget = float(input())
beer_bottles = int(input())
chips_count = int(input())

beer_price = 1.2
beers_total = beer_price * beer_bottles


chips_price = (45/100) * beers_total
chips_total = ceil(chips_price * chips_count)

total_cost = chips_total + beers_total

if budget >= total_cost:
    money_left = budget - total_cost
    print(f"{name} bought a snack and has {money_left:.2f} leva left.")

elif total_cost > budget:
    money_needed = total_cost - budget
    print(f"{name} needs {money_needed:.2f} more leva!")