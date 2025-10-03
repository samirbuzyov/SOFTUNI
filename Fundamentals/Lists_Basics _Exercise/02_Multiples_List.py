factor = int(input())
count = int(input())

lst = []

for i in range(1,1+count):
    temp = factor * i
    lst.append(temp)
    
print(lst)