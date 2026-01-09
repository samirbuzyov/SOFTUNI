def print_curr_row(spaces, stars):
    print(f'{" " * spaces}{"* " * stars}')


def print_upper_part(n:int):
    for row in range(1, n + 1):
        print_curr_row(n-row, row)

def print_down_part(n:int):
    for row in range(1, n):
        print_curr_row(row,n-row)

def print_rhombus(n:int):
    print_upper_part(n)
    print_down_part(n)

n = int(input())
print_rhombus(n)