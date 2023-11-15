def args_to_tuple(*args):
    str_list = []
    for item in args:
        if isinstance(item, str):
            str_list.append(item)
    return tuple(str_list)


print(args_to_tuple(1, 2, 3, 'a', 'b', 'c'))
