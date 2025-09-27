

while True:
    money = 0
    destination = input()
    if destination == 'End':
        break
    budget = float(input())

    while money < budget:
        new_income = float(input())
        money += new_income

    print(f'Going to {destination}!')



