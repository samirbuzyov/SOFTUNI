# inp = input().split()
# tup = tuple(float(x) for x in inp)
#
# lst = []
#
# for el in tup:
#     if el not in lst:
#         lst.append(el)
#
# for el in lst:
#     count = tup.count(el)
#     print(f'{el:.1f} - {count} times')

nums = tuple([float(el) for el in input().split()])

dict = {}

for el in nums:
    dict[el] = nums.count(el)

for key, value in dict.items():
    print(f'{key:.1f} - {value} times')