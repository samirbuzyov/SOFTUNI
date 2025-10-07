def age_assignment(*args:str, **kwargs):
    result_dict = {}
    for letter, age in kwargs.items():
        for name in args:
            if name.startswith(letter):
                if name not in result_dict:
                    result_dict[name] = age

    result = ''
    for name, age in sorted(result_dict.items(), key=lambda kvp: kvp[0]):
        result += f"{name} is {age} years old.\n"
    return result

print(age_assignment("Peter", "George", G=26, P=19))