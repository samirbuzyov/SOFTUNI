# string = input()
#
# for index in range(1, len(string)):
#     if index == 1:
#         print(string[0], end='')
#     if string[index-1] == string[index]:
#         continue
#     print(string[index], end='')
#
#
text = input()
final_string = ''
first_char = text[0]
final_string += first_char
for char in text:
    if char != final_string[-1]:
        final_string += char

print(final_string)