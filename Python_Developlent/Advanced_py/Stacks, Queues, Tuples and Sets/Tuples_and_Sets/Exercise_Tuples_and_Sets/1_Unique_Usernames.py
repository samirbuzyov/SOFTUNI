n = int(input())

set1 = set()
for _ in range(n):
    username = input()
    set1.add(username)


print(*set1, sep='\n')