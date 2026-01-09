bag = {'shards': 0, 'fragments': 0, 'motes': 0}
junk = {}
legendary_item = ""

while True:
    entry = input().split()

    for i in range(0, len(entry), 2):
        quantity = int(entry[i])
        material = entry[i + 1].lower()

        if material in bag:
            bag[material] += quantity
        else:
            junk[material] = junk.get(material, 0) + quantity

        if bag.get("shards", 0) >= 250:
            legendary_item = "Shadowmourne"
            bag["shards"] -= 250
            break
        elif bag.get("fragments", 0) >= 250:
            legendary_item = "Valanyr"
            bag["fragments"] -= 250
            break
        elif bag.get("motes", 0) >= 250:
            legendary_item = "Dragonwrath"
            bag["motes"] -= 250
            break

    if legendary_item:
        print(f"{legendary_item} obtained!")
        break

for material in ["shards", "fragments", "motes"]:
    print(f"{material}: {bag.get(material, 0)}")

for material, quantity in junk.items():
    print(f"{material}: {quantity}")
