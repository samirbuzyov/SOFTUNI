# Снимките за дългоочаквания филм "Годзила срещу Конг" започват. 
# Сценаристът Адам Уингард ви моли да напишете програма, която да изчисли, 
# дали предвидените средства са достатъчни за снимането на филма.
# За снимките  ще бъдат нужни определен брой статисти, облекло за всеки един статист и декор.
# Известно е, че:
#         ◦ Декорът за филма е на стойност 10% от бюджета. 
#         ◦ При повече от 150 статиста,  има отстъпка за облеклото на стойност 10%.


budget = float(input())
statists_count = int(input())
clothes_per_statist = float(input())
dekor = 0.1 * budget
clothes = clothes_per_statist * statists_count



if statists_count > 150:
    clothes *= 0.9


total = clothes + dekor

if budget < total:
    needed_money = total - budget
    print(f'Not enough money!\nWingard needs {needed_money:.2f} leva more.')
else:
    left_money = budget - total
    print(f'Action!\nWingard starts filming with {left_money:.2f} leva left.')