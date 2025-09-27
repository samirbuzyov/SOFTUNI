num = int(input())

# if 100 <= num <= 200 or num == 0:
#     pass

# else:
#     print('invalid')
valid = 100 <= num <= 200 or num == 0

if not valid:
    print('invalid')