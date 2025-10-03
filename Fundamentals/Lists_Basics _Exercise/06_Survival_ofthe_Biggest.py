from sys import maxsize

line = input().split()
n = int(input())



my_lst = []

for i in line:
    temp = int(i)
    my_lst.append(temp)

for i in range(n):
    min = maxsize
    for j in my_lst:
        if j < min:
            min = j

    my_lst.remove(min)




print(*my_lst, sep=', ')