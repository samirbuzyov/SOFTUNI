def sum_numbers(first:int,second:int):
    res = first + second
    return res

def subtract(result:int,third:int):
    res = result - third
    return res

def add_and_subtract(first:int,second: int,third:int):
    add = sum_numbers(first ,second)
    sub = subtract(add , third)
    return sub

first_inp = int(input())
second_inp = int(input())
third_inp = int(input())

result1 = add_and_subtract(first_inp,second_inp,third_inp)
print(result1)