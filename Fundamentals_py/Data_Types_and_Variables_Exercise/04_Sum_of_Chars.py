number_lines = int(input())
total = 0
for number in range(number_lines):
    char = input()
    total += ord(char)


print(f'The sum equals: {total}')