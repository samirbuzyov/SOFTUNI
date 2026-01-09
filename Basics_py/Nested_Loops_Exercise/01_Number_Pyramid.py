
n = int(input())
bigger_than =  False
counter =0

for row in range(1, n+1):
    for col in range(1, row + 1):
        if counter > n:
            bigger_than = True
            break

        counter += 1
        print(str(counter) + ' ', end='')

    if bigger_than:
        break
    print()