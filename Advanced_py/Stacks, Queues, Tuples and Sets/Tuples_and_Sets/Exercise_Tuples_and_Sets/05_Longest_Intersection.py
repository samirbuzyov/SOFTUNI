n = int(input())

result = []
for i in range(n):
    inpt = input().split(',')
    first_start = int(inpt[0])
    dash = inpt[1].split('-')
    first_end = int(dash[0])
    second_start = int(dash[1])
    second_end= int(inpt[2])
    set1 = set([el for el in range(first_start, first_end + 1)])
    set2 = set([el for el in range(second_start, second_end + 1)])

    result.append(set1.intersection(set2))

idx = 0
len1= 0
for i in range(len(result)):
    if len1<len(result[i]):
        len1 = len(result[i])
        idx = i

print(f"Longest intersection is {list(result[idx])} with length {len1}")



