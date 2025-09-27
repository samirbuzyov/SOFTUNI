# left_side = int(input())
# right_side = left_side
#
# sum_left_side = 0
# sum_right_side = 0
# sum_sum = 0
#
# for _ in range(left_side):
#     new_number = int(input())
#     sum_left_side += new_number
#
# for __ in range(right_side):
#     new_number_1 = int(input())
#     sum_right_side += new_number_1
#
# if sum_right_side > sum_left_side:
#     sum_sum = sum_right_side - sum_left_side
#     print(f'No, diff = {sum_sum}')
# elif sum_left_side > sum_right_side:
#     sum_sum = sum_left_side - sum_right_side
#     print(f'No, diff = {sum_sum}')
# elif sum_left_side == sum_right_side:
#     print(f'Yes, sum = {sum_right_side}')


n = int(input())
left_sum = right_sum = 0


for idx in range(n *2):
    new_number = int(input())
    if idx < n:
        left_sum += new_number
    elif idx >= n:
        right_sum += new_number

if right_sum == left_sum:
    print(f'Yes, sum = {left_sum}')
else:
    print(f'No, diff = {abs(right_sum - left_sum)}')

