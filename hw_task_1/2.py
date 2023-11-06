def the_longest_list_v1(some_list_1, some_list_2):
    length_of_first = len(some_list_1)
    length_of_second = len(some_list_2)
    if length_of_first > length_of_second:
        return length_of_first
    elif length_of_first < length_of_second:
        return length_of_second
    else:
        return "Списки равны!"


def the_longest_list_v2(some_list_1, some_list_2):
    comparator_list = []
    comparator_list.append(some_list_1)
    comparator_list.append(some_list_2)
    return len(max(comparator_list))


list_1 = [1, 2, 3, 4]
list_2 = [1, 2]

print(the_longest_list_v1(list_1, list_2))
print(the_longest_list_v2(list_1, list_2))
