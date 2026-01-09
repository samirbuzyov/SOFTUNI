products = {}

while True:
    entry = input()
    if entry == "buy":
        break

    name, price, quantity = entry.split()
    price = float(price)
    quantity = int(quantity)

    if name in products:
        products[name]["quantity"] += quantity
        products[name]["price"] = price
    else:
        products[name] = {"price": price, "quantity": quantity}

print(products)

for name, data in products.items():
    total_price = data["price"] * data["quantity"]
    print(f"{name} -> {total_price:.2f}")
