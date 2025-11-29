def reduce_function(*lst):
    pos = sum(i for i in lst if i > 0)
    neg = sum(i for i in lst if i < 0)

    result = f"{neg}\n{pos}\n"

    if pos <abs(neg):
        result+="The negatives are stronger than the positives"
    else:
        result += "The positives are stronger than the negatives"

    return result

enter = [int(el) for el in input().split()]

print(reduce_function(*enter))

