def even_odd(*args):
    nums = list(args)
    command = nums.pop()

    if command == 'even':
        return [el for el in nums if el % 2 == 0]
    else:
        return [el for el in nums if el % 2 != 0]

