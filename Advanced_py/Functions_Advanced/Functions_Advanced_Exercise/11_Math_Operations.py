from collections import deque


def math_operations(*args, **kwargs):
    numbers = deque(args)
    idx = 0
    while numbers:
        num = float(numbers.popleft())
        if idx == 0:
            kwargs["a"] += num
            idx += 1
        elif idx == 1:
            kwargs["s"] -= num
            idx += 1
        elif idx == 2:
            if num != 0:
                kwargs["d"] /= num
            idx += 1
        elif idx == 3:
            kwargs["m"] *= num
            idx = 0

    math_dict = sorted(kwargs.items(), key=lambda kvp: (-kvp[1], kvp[0]))
    result = ''
    for key, value in math_dict:
        result += f"{key}: {value:.1f}\n"

    return result




print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-

2.3), d=0, m=0))
print(math_operations(6.0, a=0, s=0, d=5, m=0))