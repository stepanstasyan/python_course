def retry_decorator(some_func):
    def wrapper(*args, **kwargs):
        result = some_func(*args, **kwargs)
        if result == 'Ошибка':
            print('Нечетное')
            even_or_odd()
            return 'Четное'
        else:
            return 'Четное'
    return wrapper


@retry_decorator
def even_or_odd():
    value = int(input('Введите число: '))
    if value % 2 == 0:
        return 'Четное'
    else:
        return 'Ошибка'


print(even_or_odd())

