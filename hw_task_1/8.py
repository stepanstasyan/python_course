def abbreviation_function(some_string):
    data_type = isinstance(some_string, str)
    abbreviation_string = ''
    symbol_num = 0
    if data_type:
        abbreviation_string += some_string[0]
        for symbol in some_string:
            symbol_num += 1
            if symbol == ' ':
                abbreviation_string += some_string[symbol_num]
    else:
        print('Введен неверный тип данных')
    return abbreviation_string


# user_string = input('Введите строку: ') - input() любой тип данных преобразует в строку,
# поэтому при его использовании проверка не будет работать

user_string = 'Comp Mech Lab'
print(abbreviation_function(user_string))
