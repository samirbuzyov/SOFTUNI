char1 = input()
char2 = input()



def char_in_range(a:str,b:str):
    int_a = ord(a)
    int_b = ord(b)



    for i in range(int_a + 1 ,int_b):
        print(chr(i), end=' ')

char_in_range(char1,char2)
