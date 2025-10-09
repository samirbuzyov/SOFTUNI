# stack = []
#
# n = int(input())
#
# for _ in range(n):
#     queries = input().split()
#
#     if queries[0] == '1':
#         num = int(queries[1])
#         stack.append(num)
#
#     elif stack:
#         if queries[0] == "2":
#             stack.pop()
#
#         elif queries[0] == "3":
#             print(max(stack))
#
#         elif queries[0] == "4":
#             print(min(stack))
# print(", ".join([str(el) for el in reversed(stack)]))
n = int(input())
my_stack = []
functions = {
    "1": lambda x: my_stack.append(int(x)),
    "2": lambda: my_stack.pop() if my_stack else None,
    "3": lambda: print(max(my_stack)) if my_stack else None,
    "4": lambda: print(min(my_stack)) if my_stack else None
}
for _ in range(n):
    query = input().split()
    functions[query[0]](*query[1:])
print(", ".join([str(x) for x in reversed(my_stack)]))
