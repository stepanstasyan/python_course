def stop_words_delete(some_string, stop_words):
    string_removed_commas = list(filter(lambda x: x != ',', some_string))
    my_string_upper_list = ''.join(list(map(lambda x: x.upper(), string_removed_commas))).split(' ')
    stop_words_upper_list = list(map(lambda x: x.upper(), stop_words))
    new_list = []
    for word in my_string_upper_list:
        if word not in stop_words_upper_list:
            new_list.append(word)
    return ' '.join(new_list)


my_string = 'I know so many programming languages: Go, python, php, c'
stop_words_list = ['Python', 'php', 'go', 'C']

print(stop_words_delete(my_string, stop_words_list))
