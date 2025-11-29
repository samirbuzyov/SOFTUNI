def even_odd_filter(**kwargs):
    for e_o, nums in kwargs.items():
        if e_o == 'even':
            kwargs[e_o] = [el for el in nums if el % 2 == 0]
        else:
            kwargs[e_o] = [el for el in nums if el % 2 != 0]

    sorted_even_odd = dict(sorted(kwargs.items(), key= lambda kvp: len(kvp[1]),reverse=True))

    return sorted_even_odd

print(even_odd_filter(

odd=[1, 2, 3, 4, 10, 5],

even=[3, 4, 5, 7, 10, 2, 5, 5, 2],

))