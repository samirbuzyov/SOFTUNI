total = 0
increase = 0
while True:
    a = input()


    if a == 'NoMoreMoney':
        break

    increase = float(a)


    if increase < 0:
        print('Invalid operation!')
        break

    total += increase

    print(f'Increase: {increase:.2f}')

print(f'Total: {total:.2f}')

