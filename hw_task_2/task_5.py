# задача сводится к определению всевозможных вариаций слагаемых числа
# например: для числа 5 это [[1, 1, 1, 1, 1], [1, 1, 1, 2], [1, 2, 2], [1, 1, 3], [2, 3], [1, 4]]
# есть условие: длина каждой ступеньки отличается -> слагаемые во вложенных списках не могут быть равны
# значит для числа 5 должны получить: [[2, 3], [1, 4]], а затем посчитать количество вложенных списков
# такая программа очень долго работает для больших чисел, но как сделать по-другому не придумалось :)

def break_to_terms(number):
    table = [[[]]] + [[] for _ in range(number)]
    for i in range(1, number):
        for j in range(i, number + 1):
            for previous_term in table[j - i]:
                table[j].append(previous_term + [i])

    return table[number]


def list_filter(some_list):
    for inner_list in some_list:
        for i in range(len(inner_list)):
            for j in range(i + 1, len(inner_list)):
                try:
                    if inner_list[i] == inner_list[j]:
                        some_list.remove(inner_list)
                    else:
                        continue
                except:
                    list_filter(list_of_terms)
    return some_list


def combinations_counter(some_list):
    counter = 0
    for item in some_list:
        counter += 1
    return counter


N = 10

list_of_terms = break_to_terms(N)
list_of_terms_filtered = list_filter(list_of_terms)
print(combinations_counter(list_of_terms_filtered))
