# На складе лежат разные фрукты в разном количестве. Нужно написать функцию, 
# которая на вход принимает любое количество названий фруктов и их количество, 
# а возвращает общее количество фруктов на складе.

def fruit(a):
    sum_fruit=0
    for i in fruits.values():
        sum_fruit+=i
    return sum_fruit    

fruits={
    'apple':5,
    'oranges':6,
    'bananas':7,
    'plums':10,
    'peaches':4
}
print('Всего: ', fruit(fruits))