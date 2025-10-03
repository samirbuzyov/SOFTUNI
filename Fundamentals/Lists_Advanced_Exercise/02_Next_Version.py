current_version = input().split('.')

first_num = int(current_version[0])
second_num = int(current_version[1])
third_num = int(current_version[2])
third_num += 1

for num_str in current_version:


    if third_num > 9:
        third_num = 0
        second_num += 1

    if second_num > 9:
        second_num = 0
        first_num += 1

next_version = f'{first_num}.{second_num}.{third_num}'
print(next_version)