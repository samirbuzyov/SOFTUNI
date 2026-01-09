def odd_even_sum(single_line:str):

    odd_sum = 0
    even_sum = 0

    for ch in single_line:
        int_value = int(ch)
        if int_value % 2 == 0:
            even_sum += int_value
        elif int_value % 2 != 0:
            odd_sum += int_value


    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"


single_line = input()

result = odd_even_sum(single_line)
print(result)