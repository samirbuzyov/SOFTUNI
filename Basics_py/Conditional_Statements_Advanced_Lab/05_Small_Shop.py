product = input()
town = input()
quanitty =float(input())

if town == 'Sofia':
    if product == 'coffee':
        print(quanitty * 0.5)
    elif product == 'water':
        print(quanitty * 0.8)
    elif product == 'beer':
        print(quanitty *  1.2 )
    elif product == 'sweets':
        print(quanitty * 1.45)
    elif product == 'peanuts':
        print(quanitty * 1.6)


if town == 'Plovdiv':
    if product == 'coffee':
        print(quanitty * 0.4)
    elif product == 'water':
        print(quanitty * 0.7)
    elif product == 'beer':
        print(quanitty *  1.15 )
    elif product == 'sweets':
        print(quanitty * 1.3)
    elif product == 'peanuts':
        print(quanitty * 1.5)

if town == 'Varna':
    if product == 'coffee':
        print(quanitty * 0.45)
    elif product == 'water':
        print(quanitty * 0.7)
    elif product == 'beer':
        print(quanitty *  1.1 )
    elif product == 'sweets':
        print(quanitty * 1.35)
    elif product == 'peanuts':
        print(quanitty * 1.55)
 