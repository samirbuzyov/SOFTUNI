phonebook= {}

while True:
    name_number = input()

    if '-' not in name_number:
        break


    name,number = name_number.split('-')
    phonebook[name] = number

searches = int(name_number)

for search in range(searches):
    searched_name = input()

    if searched_name in phonebook.keys():
        print(f"{searched_name} -> {phonebook[searched_name]}")
    else:
        print(f"Contact {searched_name} does not exist.")