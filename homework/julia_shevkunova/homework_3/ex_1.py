my_dict = {'tuple': '1, 2, 3, 4, 5', 'list': ['list1', 4, None, 23, False], 'set': {'new_elem', 23, 34, False, None},
           'ddict': {'code': 24737, 'title': "Game Designer", 'town': 'Minsk',
                     'country': 'Belarus', 'Work': 'remote'}}


print(my_dict['tuple'][-1])     # вывод на экран последнего элмента tuple
my_dict['list'].append(8)       # добавление элмента в конец списка
my_dict['list'].pop(1)          # удаление второго элмента списка
my_dict['ddict'][('i am a tuple',)] = 'addd'    # добавление элемента с ключем в словарь
my_dict['ddict'].pop('code')         # удаление элмента из словаря
my_dict['set'].add('text')      # добавление элемента в множество
my_dict['set'].remove(23)       # удаление элемента из множества
print(my_dict)      # вывод на экран словаря

