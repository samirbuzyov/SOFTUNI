class NameTooShortError(Exception):
    pass
class MustContainAtSymbolError(Exception):
    pass
class InvalidDomainError(Exception):
    pass

NAME_MIN_LEN = 5
VALID_DOMAIN = {".com", ".bg", ".org", ".net"}

while True:
    line = input()
    if line == "End":
        break
    if '@' not in line:
        raise MustContainAtSymbolError("Email must contain @")
    name, mail = line.split('@')
    if len(name) < NAME_MIN_LEN:
        raise NameTooShortError("Name must be more than 4 characters")
    something, dom = mail.split('.')
    domain = '.' + dom
    if domain not in VALID_DOMAIN:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    print("Email is valid")