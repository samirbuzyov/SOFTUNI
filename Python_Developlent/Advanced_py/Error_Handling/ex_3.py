class PasswordTooShortError(Exception):
    pass
class PasswordTooCommonError (Exception):
    pass
class PasswordNoSpecialCharactersError (Exception):
    pass
class PasswordContainsSpacesError (Exception):
    pass

def pass_too_common(pwd, specials):
    only_digits = pwd.isdigit()
    only_char = pwd.isalpha()
    only_spec = all(ch in specials for ch in pwd)
    return  only_char or only_digits or only_spec

SPECIAL_CHAR = {"@", "*", "&","%"}
MIN_PWD_LEN = 8

while True:
    line = input()
    if line == "Done":
        break

    if ' ' in line:
        raise PasswordContainsSpacesError("Password must not contain empty spaces")

    if len(line) < MIN_PWD_LEN:
        raise PasswordTooShortError("Password must contain at least 8 characters")

    if pass_too_common(line, SPECIAL_CHAR):
        raise PasswordTooCommonError("Password must be a combination of digits, letters, and special characters")

    if not any(ch in SPECIAL_CHAR for ch in line):
        raise PasswordNoSpecialCharactersError("Password must contain at least 1 special character")



    print("Password is valid")
