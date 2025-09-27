import math

a = input() 

square = 'square'
rectangle = 'rectangle'
circle = 'circle'
triangle = 'triangle'

if a == square: 
    b = float(input())
    lice = b * b
    print(f'{lice: .3f}')
elif a == rectangle:
    b = float(input())
    c = float(input())
    lice = b * c 
    print(f'{lice: .3f}')
elif a == circle:
    r = float(input())
    lice = math.pi*r**2
    print(f'{lice: .3f}')
elif a == triangle:
    b = float(input())
    c = float(input())
    lcie = b*c/2
    print(f'{lcie: .3f}')
    