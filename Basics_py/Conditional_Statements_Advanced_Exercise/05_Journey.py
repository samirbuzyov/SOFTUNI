budget = float(input())
season = input()


vacation_cost = 0
destination = ''
type_destination = ''

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        vacation_cost = 0.3 * budget
        type_destination = 'Camp'
    elif season == 'winter':
        type_destination = 'Hotel'
        vacation_cost = 0.7 * budget


elif budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        vacation_cost = 0.4 * budget
        type_destination = 'Camp'
    elif season == 'winter':
        type_destination = 'Hotel'
        vacation_cost = 0.8 * budget


elif budget > 1000:
    destination = 'Europe'
    type_destination = 'Hotel'
    vacation_cost = 0.9 * budget

else:
    print('Error')


print(f'Somewhere in {destination}')
print(f'{type_destination} - {vacation_cost:.2f}')