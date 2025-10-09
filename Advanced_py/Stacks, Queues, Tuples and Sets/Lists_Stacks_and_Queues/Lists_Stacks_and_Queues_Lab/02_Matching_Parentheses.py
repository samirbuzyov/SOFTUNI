math_problem = list(input())

stack = []

for i in range(len(math_problem)):
    if math_problem[i] == "(":
        stack.append(i)

    elif math_problem[i] == ")":
        start_idx = stack.pop()
        print(''.join(math_problem[start_idx:i+1]), end='\n')