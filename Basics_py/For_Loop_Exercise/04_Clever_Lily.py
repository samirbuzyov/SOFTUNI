Lilly_age = int(input())
washer_price = float(input())
toy_price = int(input())

sum = 0
toys = 0
money = 0


for year in range(1, Lilly_age + 1):
    if year % 2 ==0:
        money += 10
        sum += money
        sum -= 1
    elif year % 2 == 1:
        toys += 1

sum += toy_price * toys

if sum >= washer_price:
    money_left = sum - washer_price
    print(f"Yes! {money_left:.2f}")
elif sum < washer_price:
    money_needed = washer_price - sum
    print(f"No! {money_needed:.2f}")


# 1:50