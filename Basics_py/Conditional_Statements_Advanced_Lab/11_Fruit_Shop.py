fruit = input()
weekday = input()
quality = float(input())
price = 0
is_error = False


if weekday == 'Monday' or weekday == 'Tuesday' or weekday == 'Wednesday' or weekday == 'Thursday' or weekday == 'Friday':
    if fruit == 'banana':
        price = 2.50
    elif fruit == 'apple':
        price = 1.2
    elif fruit == 'grapefruit':
        price = 1.45
    elif fruit == 'orange':
        price = 0.85
    elif fruit == 'kiwi':
        price =2.7
    elif fruit == 'pineapple':
        price = 5.5
    elif fruit == 'grapes':
        price = 3.85
    else:
        is_error = True


elif weekday == 'Saturday' or weekday == 'Sunday':
    if fruit == 'banana':
        price = 2.70
    elif fruit == 'apple':
        price = 1.25
    elif fruit == 'grapefruit':
        price = 1.60
    elif fruit == 'orange':
        price = 0.9
    elif fruit == 'kiwi':
        price =3
    elif fruit == 'pineapple':
        price = 5.6
    elif fruit == 'grapes':
        price = 4.2
    else:
        is_error = True

    
else:
    is_error = True

total_price = price * quality

if is_error == True:
    print('error')
else:
    print(f'{total_price:.2f}')