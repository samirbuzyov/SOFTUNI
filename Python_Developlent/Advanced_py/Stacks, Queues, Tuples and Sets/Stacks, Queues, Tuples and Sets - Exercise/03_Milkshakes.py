from collections import deque

chocolate = [int(el) for el in input().split(", ")]
cups_milk = deque(int(el) for el in input().split(", "))

milkshake_count = 0

while chocolate and cups_milk and milkshake_count < 5:

    current_choc = chocolate[-1]
    current_milk = cups_milk[0]

    if current_choc <= 0 and current_milk <= 0:
        chocolate.pop()
        cups_milk.popleft()
        continue

    if current_choc <= 0:
        chocolate.pop()
        continue

    if current_milk <= 0:
        cups_milk.popleft()
        continue

    if current_choc == current_milk:
        chocolate.pop()
        cups_milk.popleft()
        milkshake_count += 1
    else:
        cups_milk.rotate(-1)
        chocolate[-1] -= 5
        if chocolate[-1] <= 0:
            chocolate.pop()
            continue


if milkshake_count == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolate:
    print(f"Chocolate: {', '.join(str(x) for x in chocolate)}")
else:
    print("Chocolate: empty")

if cups_milk:
    print(f"Milk: {', '.join(str(x) for x in cups_milk)}")
else:
    print("Milk: empty")
