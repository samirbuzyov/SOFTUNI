box_clothes = [int(x) for x in input().split()]
rack_capacity = int(input())

rack_count = 0
temp = 0

while box_clothes:
    if temp + box_clothes[len(box_clothes) - 1] > rack_capacity:
        rack_count+= 1
        temp = 0

    temp += box_clothes.pop()
if temp > 0:
    rack_count+=1
print(rack_count)