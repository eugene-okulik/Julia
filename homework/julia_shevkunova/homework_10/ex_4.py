PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
ручка 120р
пенал 300р
рюкзак 500р'''

x = PRICE_LIST.split()
elements_list = []
price_list = []
for x in x:
    if x.endswith('р'):
        price_list.append(x)
    else:
        elements_list.append(x)

new_dict = dict(zip(elements_list, price_list))
print(new_dict)
