n = int(input())
a = 1

while True:
    print(a)
    k = 2*a + 1
    a = k
    if k <= n:
        continue
    else:
        break
