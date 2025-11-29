from collections import deque

bees = deque(int(el) for el in input().split())
nectar = [int(el) for el in input().split()]
operations = deque(el for el in input().split())

honey_collected = 0

calculation = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b if b != 0 else 0
}


while bees and nectar:
    if bees[0] > nectar[-1]:
        nectar.pop()
    else:
        operation = operations.popleft()
        honey_collected += abs(calculation[operation](bees[0], nectar[-1]))
        nectar.pop()
        bees.popleft()

print(f"Total honey made: {honey_collected}")
if bees:
    print(f'Bees left: {", ".join(str(el) for el in bees)}')
if nectar:
    print(f'Nectar left: {", ".join(str(el) for el in nectar)}')