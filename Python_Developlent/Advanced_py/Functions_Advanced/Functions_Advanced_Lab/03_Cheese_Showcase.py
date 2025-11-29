def sorting_cheeses(**kwargs):
    cheeses_dict = sorted(kwargs.items(), key= lambda kvp: (-len(kvp[1]),kvp[0]))
    # result = ''
    # for cheese_name,cheese_quantity in sorted_cheeses:
    #     result+= cheese_name + '\n'
    #     for quantity in sorted(cheese_quantity, reverse= True):
    #         result += str(quantity) + '\n'
    #
    # return result
    # result = []
    #
    # for cheese_name, quantities in cheeses_dict:
    #     result.append(cheese_name)
    #     quantity_list = sorted(quantities, reverse= True)
    #     result += quantity_list
    #
    # return '\n'.join([str(x) for x in result])

    result = {}

    for cheese_name, quantities in cheeses_dict:
        quantity_list = sorted(quantities, reverse=True)
        result[cheese_name] = quantity_list

    output_lines = []
    for cheese_name, quantity_list in result.items():
        output_lines.append(cheese_name)
        output_lines.extend(str(q) for q in quantity_list)

    return '\n'.join(output_lines)


print(

sorting_cheeses(

Parmesan=[102, 120, 135],

Camembert=[100, 100, 105, 500, 430],

Mozzarella=[50, 125],

)

)