n = int(input())
sum_even = 0
sum_odd = 0


for idx in range(n):
    new_number = int(input())
    if idx % 2 == 0:
        sum_even += new_number
    elif idx % 2 == 1:
        sum_odd += new_number

diff = sum_odd - sum_even

if sum_odd == sum_even:
    print('Yes')
    print(f'Sum = {sum_even}')
elif sum_even != sum_odd:
    print('No')
    print(f'Diff = {abs(diff)}')

