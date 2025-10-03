# some_text = input()
#
# for char in some_text:
#     a = ord(char)
#     b = a + 3
#     c = chr(b)
#     print(c,end='')

some_text = input()
encrypted = ''

for char in some_text:
    a = ord(char)
    b = a + 3
    c = chr(b)
    encrypted += c
print(encrypted)