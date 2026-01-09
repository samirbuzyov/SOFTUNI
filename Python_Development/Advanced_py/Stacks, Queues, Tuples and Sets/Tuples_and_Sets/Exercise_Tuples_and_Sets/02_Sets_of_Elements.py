enter = input().split()

n = int(enter[0])
m = int(enter[1])

set1 = set()
set2 = set()

for i in range(n):
    user = int(input())
    set1.add(user)

for i in range(m):
    user = int(input())
    set2.add(user)

result = set1.intersection(set2)
print(*result,sep='\n')