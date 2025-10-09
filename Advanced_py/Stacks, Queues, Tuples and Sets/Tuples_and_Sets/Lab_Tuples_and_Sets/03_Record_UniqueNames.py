n = int(input())

set_lst = set()

for _ in range(n):
    name = input()
    set_lst.add(name)

for name in set_lst:
    print(name)