from sys import maxsize

new_input = input()
max_number = -maxsize

# while new_input != 'Stop':
#     int_input = int(new_input)
#     if max_number < int_input:
#         max_number = int_input
#     new_input = input()
#
# print(max_number)

while True:

    if new_input == 'Stop':
        break

    int_new_input = int(new_input)

    if max_number < int_new_input:
        max_number = int_new_input

    new_input = input()


print(max_number)