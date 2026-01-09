
def check_if_palindrome(chislo:int):

    temp = str(chislo)

    a = temp == temp[::-1]

    return a

line = input().split(', ')

int_lst = []

for ch in line:
    int_lst.append(int(ch))

for i in int_lst:
    print(check_if_palindrome(i))






