from collections import deque

dq = deque([])
count = 0
while True:
    receive = input()
    if receive == "End":
        print(f'{count} people remaining.')
        break
    elif receive == "Paid":
        for name in range(len(dq)):
            print(dq.popleft())
            count -=1
    else:
        dq.append(receive)
        count+= 1