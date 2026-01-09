n = int(input())

set1 = set()
for i in range(n):
    enter = input().split()

    for idx in range(len(enter)):
        set1.add(enter[idx])

print(*set1, sep='\n')