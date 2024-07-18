PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
ручка 120р
пенал 300р
рюкзак 500р'''


split_list = PRICE_LIST.split()
price_list = [x for x in split_list if x.endswith('р')]
elements_list = [x for x in split_list if not x.endswith('р')]
new_dict = dict(zip(elements_list, price_list))
print(new_dict)

