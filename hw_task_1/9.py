def factorial_finder(some_number):
    numbers_list = []
    counter = some_number - 1
    for num in range(some_number):
        numbers_list.append(some_number)
        some_number -= 1
    while counter > 0:
        new_number = numbers_list[counter] * numbers_list[counter - 1]
        numbers_list[counter - 1] = new_number
        counter -= 1
    return numbers_list[0]


print(factorial_finder(5))
