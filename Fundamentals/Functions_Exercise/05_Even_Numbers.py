def is_even(current_number:int):
    return current_number % 2 == 0


line_str = input().split()

lst_int = []

for ch in line_str:
    lst_int.append(int(ch))

final_result = list(filter(is_even,lst_int))

print(final_result)