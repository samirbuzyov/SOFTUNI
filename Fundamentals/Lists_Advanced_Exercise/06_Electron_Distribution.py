number_elctrons = int(input())

position = 1
new_lst = []
while number_elctrons>0:
    max_electrons = 2 * (position **2)

    if max_electrons > number_elctrons:
        new_lst.append(number_elctrons)
        break

    new_lst.append(max_electrons)
    number_elctrons -= max_electrons
    position += 1

print(new_lst)
