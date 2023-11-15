def divisible_func(some_value, some_list):
    new_list = list(filter(lambda x: x % some_value == 0, some_list))
    return new_list


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_value = 2

print(divisible_func(my_value, my_list))
