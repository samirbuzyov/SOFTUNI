username = input()
password = input()


while True:
    password_for_sign_in = input()
    if password != password_for_sign_in:
        continue
    else:
        print(f'Welcome {username}!')
        break



