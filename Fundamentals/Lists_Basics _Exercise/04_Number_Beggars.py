money = input().split(', ')
beggars = int(input())

lst_money = []

new_lst = []
for m in money:
    lst_money.append(int(m))

for i in range(beggars):
    temp = 0

    for j in range(i,len(lst_money), beggars):
        temp += lst_money[j]

    new_lst.append(temp)
print(new_lst)