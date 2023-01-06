# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19



import random

my_list = []
new_list = []
for item in range(random.randint(5, 10)):
    num = random.uniform(0, 10)
    my_list.append(round(num, 2))
    num_ad = my_list[item] % 1
    new_list.append(round(num_ad, 2))

print(my_list)
print(f'{max(new_list)} - {min(new_list)} = {round(max(new_list) - min(new_list),2)}')