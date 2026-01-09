N = int(input())

for num in range(1111, 10000):
    num_str = str(num)
    is_special = True

    for digit_char in num_str:
        digit = int(digit_char)

        if digit == 0 or N % digit != 0:
            is_special = False
            break

    if is_special:
        print(num, end=" ")
