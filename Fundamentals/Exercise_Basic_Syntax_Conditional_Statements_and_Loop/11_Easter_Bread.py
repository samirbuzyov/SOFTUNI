budget = float(input())

flour_kg_price = float(input())
egg_pack_price = flour_kg_price *0.75
milk_liter_price = flour_kg_price * 1.25


bread_price = flour_kg_price + egg_pack_price + milk_liter_price*0.25

colored_eggs = 0

loaf_count = 0


while budget > bread_price:

    budget -= bread_price
    loaf_count += 1

    colored_eggs += 3


    if loaf_count % 3 == 0:
        temp = loaf_count - 2
        colored_eggs -= temp

print(f"You made {loaf_count} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")



