quantity = int(input())
days = int(input())


decorations_price = 0
decorations_points =0


ornament_price = 2
ornament_points = 5

skirt_price = 5
skirt_points = 3

garland_price =3
garland_points = 10

lights_price = 15
lights_points = 17
for day in range(1, days + 1):

    if day %11 == 0:
        quantity += 2

    if day % 5 == 0:
        decorations_price += quantity * lights_price
        decorations_points +=  lights_points


    if day % 3 == 0:
        decorations_price += ( skirt_price+ garland_price) * quantity
        decorations_points += (skirt_points + garland_points)


    if day % 2 == 0:
        decorations_price += ornament_price * quantity
        decorations_points += ornament_points


    if day % 3 == 0 and day % 5 == 0:
        decorations_points += 30




    if day % 10 == 0:
        decorations_points -= 20

        decorations_price += skirt_price + garland_price + lights_price
    if day ==days:
        if days % 10== 0 and days > 9:
            decorations_points -= 30

print(f"Total cost: {decorations_price}")
print(f"Total spirit: {decorations_points}")




