my_dict = {'Nikita': 2007, 'Sasha': 2001, 'Andrey': 1998}
print(my_dict)
print(my_dict['Nikita'])
print(my_dict.get('Misha', 'Такого ключа нет!'))
my_dict.update({'Roma': 1995, 'Evgeniy': 2015})
print(my_dict.pop('Sasha'))
print(my_dict)
my_set = {'string', 1, 5, 7, 1, 1, 5, (152,173), True,'string'}
print(my_set)
my_set.add(51)
my_set.add('72')
my_set.discard(1)
print(my_set)