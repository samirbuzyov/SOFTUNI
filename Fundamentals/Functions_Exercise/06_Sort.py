def sort(lst:list):

    return sorted(lst)


line = input().split()

line_lst=[]

for i in line:
    line_lst.append(int(i))

result = sort(line_lst)
print(result)