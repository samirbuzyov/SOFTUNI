def smallest_number(num_lst: list) -> int:
    return min(num_lst)


first = int(input())
second = int(input())
third = int(input())

smallest_of_three = smallest_number([first, second,third])

print(smallest_of_three)