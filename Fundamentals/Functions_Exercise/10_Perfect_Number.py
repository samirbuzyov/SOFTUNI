def perfect_number(number:int):
    if number <= 0:
        return "It's not so perfect."


    elif number % 2 != 0:
        return "It's not so perfect."

    devisor_sum = 0

    for i in range(1, number // 2):
        if number % i == 0:
            devisor_sum += i


    if number // 2 == devisor_sum:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."





a = int(input())

is_isnot_perfect = perfect_number(a)

print(is_isnot_perfect)