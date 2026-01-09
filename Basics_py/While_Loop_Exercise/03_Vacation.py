#
# vacation_cost = float(input())
# money = float(input())
#
# days = 0
# spend_days = 0
#
# while True:
#     days += 1
#
#     action = input()
#     amount = float(input())
#
#     if action == "spend":
#         money -= amount
#         if money < 0:
#             money = 0
#         spend_days += 1
#
#         if spend_days == 5:
#             print("You can't save the money.")
#             print(f"{days}")
#             break
#
#     elif action == "save":
#         money += amount
#         spend_days = 0
#
#     if money >= vacation_cost:
#         print(f"You saved the money for {days} days.")
#         break


vacation_cost = float(input())
money = float(input())

have_the_money = False
days = spend_days = 0

while money < vacation_cost:
    action = input()
    save_spend_money = float(input())

    days += 1

    if action == 'spend':
        money -= save_spend_money
        if money < save_spend_money:
            money = 0
            continue

        spend_days += 1
        if spend_days == 5:
            print("You can't save the money.")
            print(spend_days)
            break

    elif action == 'save':
        money += save_spend_money

if money >= vacation_cost:
    print(f"You saved the money for {days} days.")