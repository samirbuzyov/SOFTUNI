

LITER = 1 * 1

length = int(input())
width = int(input())
height = int(input())
percent = float(input()) / 100
obem = length * width * height / 1000

liter = (1 - percent) * obem

print(liter)

# 2.31.00