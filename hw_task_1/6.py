def positive_values(some_list):
    positive_counter = 0
    for i in some_list:
        if i > 0:
            positive_counter += 1
        else:
            continue
    print(positive_counter)


my_list = [-1, -2, -3.5, 0, 2, 52, 100]
positive_values(my_list)
