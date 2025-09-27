# В една кинозала столовете са наредени в правоъгълна форма в r реда и c колони. Има три вида прожекции с билети на различни цени:
screen_type = input()
r = int(input())
c = int(input())
total_sits = r  * c
income = 0
ticket_price = 0



# •	Premiere - премиерна прожекция, на цена 12.00 лева;

if screen_type == 'Premiere':
    ticket_price = 12
    income = ticket_price * total_sits
    print(f'{income:.2f} leva')


# •	Normal - стандартна прожекция, на цена 7.50 лева;
if screen_type == 'Normal':
    ticket_price = 7.5
    income = ticket_price * total_sits
    print(f'{income:.2f} leva')

# •	Discount - прожекция за деца, ученици и студенти на намалена цена от 5.00 лева.
if screen_type == 'Discount':
    ticket_price = 5
    income = ticket_price * total_sits
    print(f'{income:.2f} leva')

# Напишете програма, която чете тип прожекция (текст), брой редове и брой колони в залата (цели числа), въведени от потребителя,
# и изчислява общите приходи от билети при пълна зала. Резултатът да се отпечата във формат 2 знака след десетичната точка.
