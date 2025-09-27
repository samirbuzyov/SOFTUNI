# from sys import maxsize
#
# numbers_count = int(input())
#
# total_sum = 0
# biggest_num = -maxsize
#
# for _ in range(numbers_count):
#     current_number = int(input())
#
#     total_sum += current_number
#     if biggest_num < current_number:
#         biggest_num = current_number
#
# answer = total_sum / 2
# diff = biggest_num - (total_sum - biggest_num)
#
# if biggest_num == answer:
#     print('Yes')
#     print(f'Sum = {int(answer)}')
# else:
#     print('No')
#     print(f'Diff = {abs(int(diff))}')
#


from sys import maxsize
sum = 0
biggest_number = -maxsize
count_numbers = int(input())

for _ in range(count_numbers):
    current_number = int(input())
    sum += current_number
    if current_number > biggest_number:
        biggest_number = current_number


if sum - biggest_number == biggest_number:
    print(f'Yes')
    print(f'Sum = {sum//2}')
else:
    diff = sum - 2 * biggest_number
    print('No')
    print(f'Diff = {abs(diff)}')
