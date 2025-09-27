# num_open_tabs = int(input())
# salary = float(input())
#
#
# fine = 0
#
# for tabs in range(num_open_tabs):
#     open_tab = input()
#
#     if open_tab == 'Facebook':
#         fine += 150
#     elif open_tab == 'Instagram':
#         fine += 100
#     elif open_tab == 'Reddit':
#         fine += 50
#     else:
#         fine += 0
#
# if salary <= fine:
#     print('You have lost your salary.')
# elif fine < salary:
#     print(round(salary - fine))
#
#
num_open_tabs = int(input())
salary = float(input())




for tabs in range(num_open_tabs):
    open_tab = input()
    if open_tab == 'Facebook':
        salary -= 150
    elif open_tab == 'Instagram':
        salary -= 100
    elif open_tab == 'Reddit':
        salary -= 50

    if salary <= 0:
        print('You have lost your salary.')
        break


if salary > 0:
    print(round(salary))
