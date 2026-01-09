a = input()
b = input()

last_str = a


for i in range(len(a)):

    first = b[0:i+1]
    second = a[i+1: ]

    new_str = first + second

    if new_str != last_str:
        print(new_str)

    last_str = new_str


