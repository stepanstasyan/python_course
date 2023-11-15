def list_intersection(some_list_1, some_list_2):
    intersection_list = []
    for item in some_list_1:
        if item in some_list_2:
            intersection_list.append(item)
    return intersection_list


def list_intersection_2(some_list_1, some_list_2): # вернет в пересечение, но порядок элементов не сохранится
    return (list(set(some_list_1) & set(some_list_2)))


list_1 = [1, 2, 3, 11, 12, 13, 'один', 'два']
list_2 = [1, 2, 3, 101, 102, 103, 'один', 'три']

print(list_intersection(list_2, list_1))
print(list_intersection_2(list_2, list_1))
