def int_check(some_func):
    def wrapper(*args, **kwargs):
        result = some_func(*args, **kwargs)
        if isinstance(result, int):
            return result
        else:
            raise TypeError("Неверный тип данных")
    return wrapper


@int_check
def first_function(some_number):
    return some_number * 3

@int_check
def second_function(some_number):
    return some_number + 3


print(first_function(5))
print(second_function(5.1))

