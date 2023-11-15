import time

def time_measurement(some_func):
    def wrapper(*args, **kwargs):
        t0 = time.time()
        result = some_func(*args, **kwargs)
        t1 = time.time() - t0
        return f'Результат: {result}, время выполнения: {round(t1, 3)} сек'

    return wrapper


@time_measurement
def squares_calc(some_list):
    time.sleep(1)
    return list(map(lambda x: x * 2, some_list))


my_list = list(range(1, 11))
print(squares_calc(my_list))
