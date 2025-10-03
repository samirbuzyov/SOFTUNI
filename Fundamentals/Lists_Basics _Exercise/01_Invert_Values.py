to_be_list = input().split()
negative_list = []


for i in to_be_list:
    new_element = -1 * int(i)
    negative_list.append(new_element)

print(negative_list)