entry = input().split()
bag = {'Shards' : 0, 'Fragments' : 0, 'Motes' : 0}

has_won = False

for i in range(0, len(entry), 2):
    material = entry[i + 1]
    quantity = int(entry[i])

    if material in bag.keys():
        bag[material] += quantity
    else:
        bag[material] = quantity


for material, quantity in bag.items():
    if quantity > 250:
        if material == 'Shards':
            quantity -= 250
            has_won = True

        if material == 'Fragments':
            pass
        if material == 'Motes':
            pass

