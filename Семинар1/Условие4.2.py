# 4.2 Найдите выручку компании в зависимости от месяца
# Для этого напишите функцию, которая на вход принимает список с датами и 
# список с выручкой, а на выходе словарь, где ключи - это месяцы, а значения - 
# это выручка.
# Используйте аннотирование типов.

def create_dict(purchases, sum_purchases):
    new_dict = {}
    for i in range(len(purchases)):
        new_dict[purchases[i]] = sum_purchases[i]
    return new_dict

list_new=create_dict(purchases, sum_purchases)
list_new