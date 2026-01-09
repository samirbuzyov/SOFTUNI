num_cities = int(input())

total_profit = 0

for city in range(1, num_cities + 1):
    name = input()
    earned_money = float(input())
    expenses = float(input())
    city_expenses = expenses

    is_third = False

    city_profit = 0

    if city % 3 == 0 and city > 2:
        city_expenses += expenses * 0.5
        is_third = True


    if city % 5 == 0 and city > 4:
        earned_money -= 0.1 * earned_money
        if is_third:
            city_expenses = expenses

    city_profit += earned_money
    city_profit -= city_expenses
    total_profit += city_profit

    print(f"In {name} Burger Bus earned {city_profit:.2f} leva.")

print(f"Burger Bus total profit: {total_profit:.2f} leva.")
