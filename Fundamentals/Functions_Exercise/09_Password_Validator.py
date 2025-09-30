def password_validator(password:str):

    errors = []
    if len(password) < 6 or len(password) > 10:
        errors.append("Password must be between 6 and 10 characters")


    elif not password.isalnum():
        errors.append("Password must consist only of letters and digits")

    count = 0
    for ch in password:
        if ch.isdigit():
            count+= 1


    if count < 2:
        errors.append("Password must have at least 2 digits")


    if not errors:
        print("Password is valid")
    else:
        print('\n'.join(errors))

passs = input()


password_validator(passs)