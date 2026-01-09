def factorial(n:int) -> int:
    if n == 1:
        return n

    result = n*factorial(n - 1)
    return result

n = int(input())
print(factorial(n))