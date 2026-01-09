

text = input()
sum = 0

#
# for char in text:
#     if char == 'a':
#         sum += 1
#
#     elif char == 'e':
#         sum += 2
#
#     elif char == 'i':
#         sum += 3
#
#     elif char == 'o':
#         sum += 4
#
#     elif char == 'u':
#         sum += 5
#
# print(sum)

for i in range(0, len(text)):
    if text[i] == 'a':
        sum += 1
    elif text[i] == 'e':
        sum += 2
    elif text[i] == 'i':
        sum += 3
    elif text[i] == 'o':
        sum += 4
    elif text[i] == 'u':
        sum += 5

print(sum)