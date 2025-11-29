def calc_sum(numbers: list[int], idx: int)-> int:
    if idx == len(numbers) - 1:
        return numbers[idx]

    result = numbers[idx] + calc_sum(numbers, idx + 1)
    return result

array = [int(el) for el in input().split()]
idx = 0

print(calc_sum(array,idx))