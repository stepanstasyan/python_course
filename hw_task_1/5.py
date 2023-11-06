def yes_or_no(some_string_1, some_string_2):
    if some_string_1 in some_string_2:
        print('ДА')
    else:
        print('НЕТ')


str_1 = 'test'
str_2 = 'test1'

yes_or_no(str_1, str_2)
