n = int(input())

info = set()
for _ in range(n):
    command, number = input().split(', ')
    if command == 'IN':
        info.add(number)
    elif command == 'OUT':
        info.remove(number)

if not info:
    print("Parking Lot is Empty")
else:
    print(*info, sep='\n')