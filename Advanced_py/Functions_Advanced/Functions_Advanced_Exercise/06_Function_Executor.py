def func_executor(*args):
    result = ''
    for execution in args:
        func = execution[0]
        func_args = execution[1]
        func_result = func(*func_args)
        result+=f"{func.__name__} - {func_result}\n"
    return result
def make_upper(*strings):

    result = tuple(s.upper() for s in strings)

    return result


def make_lower(*strings):

    result = tuple(s.lower() for s in strings)

    return result


print(func_executor(

(make_upper, ("Python", "softUni")),

(make_lower, ("PyThOn",)),

))