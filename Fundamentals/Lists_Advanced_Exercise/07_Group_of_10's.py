sequence = input().split(', ')

group = 0

for neznam in sequence:
    num = int(neznam)
    if num > group:
        group = num

if group // 10 == group / 10:
    group = group // 10
else:
    group = group// 10 + 1

a = 0
for gr in range(1, group + 1):

    lst = []
    for neznam in sequence:
        num = int(neznam)
        if  a<num <= gr * 10:
            lst.append(num)




    a+=10

    print(f"Group of {gr}0's: {lst}")
