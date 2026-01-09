command = ''
count_coffees = 0
while True:
    command = input()
    if command == 'END':
        break
    elif command == 'dog' or command == 'cat' or command == 'coding' or command == 'movie':
        count_coffees += 1

    elif command == 'DOG' or command == 'CAT' or command == 'CODING' or command == 'MOVIE':
        count_coffees += 2


if count_coffees >5 :
    print('You need extra sleep')
else:
    print(count_coffees)