def list_upgrade(some_list, some_value):
    some_list.append(some_value)
    return some_list


my_list = [1, 'два', 3.5]
value = 4

print(list_upgrade(my_list, value))
