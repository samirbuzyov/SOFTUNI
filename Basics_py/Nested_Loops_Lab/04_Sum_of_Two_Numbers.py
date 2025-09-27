start_num = int(input())
end_num = int(input())
magic_num = int(input())

count = 0
is_equal = False

for num_1 in range(start_num, end_num+1):
    for num_2 in range(start_num, end_num + 1):
        count += 1
        if num_2 + num_1 == magic_num:
            print(f"Combination N:{count} ({num_1} + {num_2} = {magic_num})")
            is_equal = True
            break


    if is_equal:
        break

if not is_equal:
    print(f"{count} combinations - neither equals {magic_num}")