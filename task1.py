# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


import random

def find_elem():
    res=0
    my_list=[random.randint(1,10) for item in range (random.randint(3,10))]
    new_list=my_list[1:random.randint(3,10):2]
    res=sum(new_list)
    print(my_list)
    print(new_list)
    print(f'Answer is: {res}')
    
find_elem()



