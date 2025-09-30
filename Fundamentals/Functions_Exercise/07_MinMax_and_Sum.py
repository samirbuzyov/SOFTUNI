def mmin(lst:list):
    mini = min(lst)
    return f"The minimum number is {mini}"

def maxx(lst:list):
    maxi = max(lst)
    return f"The maximum number is {maxi}"

def summ(lst:list):
    suma = 0
    for i in lst:
        suma+= i

    return f"The sum number is: {suma}"

line = input().split()

line_lst = []
for i in line:
    line_lst.append(int(i))

result_min = mmin(line_lst)
result_max = maxx(line_lst)
result_sum = summ(line_lst)

print(result_min)
print(result_max)
print(result_sum)