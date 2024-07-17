#Работа со словарями
mi_dict = {'Tanya': 1989, 'Sasha': 1987}
print(mi_dict)
print(mi_dict['Sasha'])
print(mi_dict.get('Ira'))
mi_dict.update({'Dima': 1985, 'Kiril': 1988})
mi_dict.pop('Sasha')
print(mi_dict.get('Sasha'))
print(mi_dict)

# Работа с множествами
my_set = {6, 5, 4, 5, (5, True, 'd'), 'd', 'f'}
print(my_set)
my_set.update({'a', 18})
my_set.discard((5, True, 'd'))
print(my_set)