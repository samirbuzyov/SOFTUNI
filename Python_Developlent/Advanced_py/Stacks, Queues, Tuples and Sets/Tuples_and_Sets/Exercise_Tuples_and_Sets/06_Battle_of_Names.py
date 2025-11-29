n = int(input())

odd_numbers = set()
even_numbers = set()

for i in range(n):
    txt = input()
    suma = 0
    for char in txt:
        suma += ord(char)

    suma //= i+1
    if suma % 2 ==0:
        even_numbers.add(suma)
    else:
        odd_numbers.add(suma)

if sum(even_numbers) > sum(odd_numbers):
    print(*even_numbers.symmetric_difference(odd_numbers),sep= ', ')
elif sum(even_numbers) < sum(odd_numbers):
    print(*odd_numbers.difference(even_numbers),sep= ', ')
else:
    print(*even_numbers.union(odd_numbers),sep= ', ')