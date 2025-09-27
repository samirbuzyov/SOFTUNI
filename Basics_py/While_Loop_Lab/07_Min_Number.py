from sys import maxsize

new_input = input()
min_number = maxsize

while new_input != 'Stop':
    int_new_input = int(new_input)

    if min_number > int_new_input:
        min_number = int_new_input

    new_input = input()

print(min_number)

