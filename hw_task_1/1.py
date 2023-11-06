def string_length(some_string):
    sum = 0
    for symbol in some_string:
        sum += 1
    return sum


print(f'Длина строки: {string_length("abcd")}')
