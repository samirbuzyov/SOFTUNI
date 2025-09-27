type_of_flowers = input()
num_flowers = int(input())
budget = int(input())


price_flowers = 0.0

discount = 1

if type_of_flowers == 'Roses':
    price_flowers = 5
    if num_flowers > 80:
        discount -= 0.1

elif type_of_flowers == 'Dahlias':
    price_flowers = 3.8
    if num_flowers > 90:
        discount -= 0.15

elif type_of_flowers == 'Tulips':
    price_flowers = 2.8
    if num_flowers >80:
        discount -= 0.15

elif type_of_flowers == 'Narcissus':
    price_flowers = 3
    if num_flowers < 120:
        discount += 0.15


elif type_of_flowers == 'Gladiolus':
    price_flowers = 2.5
    if num_flowers < 80:
        discount += 0.2

price = price_flowers * num_flowers
total_price = discount* price


if budget >= total_price:
    left_money = budget - total_price
    print(f"Hey, you have a great garden with {num_flowers} {type_of_flowers} and {left_money:.2f} leva left.")

elif budget < total_price:
    needed_money = total_price - budget
    print(f"Not enough money, you need {needed_money:.2f} leva more.")