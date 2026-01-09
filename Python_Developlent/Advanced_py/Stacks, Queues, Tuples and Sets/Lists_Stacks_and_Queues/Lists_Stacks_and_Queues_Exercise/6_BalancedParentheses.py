from collections import deque

sequence = input()

par = {"(" : ")", "[" : "]", "{": "}"}
stack = []

for char in sequence:
    if char in par:
        stack.append(char)

    elif char in par.values():
        if not stack:
            print("NO")
            break
        last_opening = stack.pop()
        if par[last_opening] != char:
            print("NO")
            break

else:
    if stack:
        print("NO")
    else:
        print("YES")

