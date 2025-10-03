def len_valid(name:str) -> bool:
    if 3 <= len(name) <= 16:
        return True
    return False

def symbols_valid(name:str) -> bool:
    for symbols in name:
        if not (symbols.isalnum() or symbols == '-' or symbols == '_'):
            return False
    return True

def redundant_valid(name:str)-> bool:
    if ' ' in name:
        return False
    return True

def username_is_valid(name : str):
    if len_valid(name)\
            and symbols_valid(name) and \
            redundant_valid(name):
        return True
    return False



read = input().split(', ')
for username in read:
    if username_is_valid(username):
        print(username)


