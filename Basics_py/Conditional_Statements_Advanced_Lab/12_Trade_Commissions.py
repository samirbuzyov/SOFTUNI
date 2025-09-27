# Напишете конзолна програма, която чете име на град (текст) и обем на продажби (реално число), въведени от потребителя,
# и изчислява и извежда размера на търговската комисионна според горната таблица.
# Резултатът да се изведе форматиран до 2 цифри след десетичната точка.
# При невалиден град или обем на продажбите (отрицателно число) да се отпечата "error". 


town = input()
sells = float(input())
comission = 0
is_error = False

if town == 'Sofia':
    if 0 <= sells <= 500:
        comission = 5/100 * sells

    elif 500 < sells <= 1000:
        comission = 7/100 * sells

    elif 1000 < sells <= 10000:
        comission = 8/100 * sells

    elif sells > 10000:
        comission = 12/100 * sells
    else:
        is_error = True




elif town == 'Varna':
    if 0 <= sells <= 500:
        comission = 4.5/100 * sells

    elif 500 < sells <= 1000:
        comission = 7.5/100 * sells

    elif 1000 < sells <= 10000:
        comission = 10/100 * sells

    elif sells > 10000:
        comission = 13/100 * sells
    else:
        is_error = True



elif town == 'Plovdiv':
    if 0 <= sells <= 500:
        comission = 5.5/100 * sells

    elif 500 < sells <= 1000:
        comission = 8/100 * sells

    elif 1000 < sells <= 10000:
        comission = 12/100 * sells

    elif sells > 10000:
        comission = 14.5/100 * sells
    else:
        is_error = True

else:
    is_error = True

if is_error == True:
    print('error')

elif is_error == False:
    print(f'{(comission) :.2f}')