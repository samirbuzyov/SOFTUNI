from collections import deque

names = input().split()

n = int(input())

queue = deque(names)

while len(queue) != 1:
    queue.rotate(-(n - 1))
    print(f"Removed {queue.popleft()}")

print(f"Last is {queue.popleft()}")