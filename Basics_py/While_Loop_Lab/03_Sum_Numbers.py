#
# number = int(input())
# new_number = int(input())
#
# sum = 0
#
# while sum < number:
#     sum += new_number
#     new_number = int(input())
#
# print(sum)

number = int(input())


sum = 0

while True:
    new_number = int(input())
    sum += new_number
    if sum < number:
        continue
    else:
        break

print(sum)