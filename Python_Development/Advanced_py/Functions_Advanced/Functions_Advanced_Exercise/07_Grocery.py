def grocery_store(**kwargs):
    result_lst = {}
    for products_name, quantity in kwargs.items():
        if products_name not in result_lst:
            result_lst[products_name] = int(quantity)
    result_lst = sorted(result_lst.items(), key=lambda kvp: (-kvp[1], -len(kvp[0]), kvp[0]))

    result_string = ''
    for products_name, quantity in result_lst:
        result_string += f"{products_name}: {quantity}\n"
    return result_string


print(grocery_store(

bread=2,

pasta=2,

eggs=20,

carrot=1,

))