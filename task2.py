# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]



from math import ceil

a=[]
al=int(input("enter len"))

for item in range(al):
    a.append (int(input(f'{item+1}')))
print(a)

na=[]
for j in range(ceil(al/2)):
    na.append(a[j]*a[-j-1])
print(na)

















# from math import ceil

# a = []
# len_ls = int(input('Введите длину списка: '))
# for item in range(len_ls):
#     a.append(int(input(f'Введите {item + 1} число: ')))
# print(a)

# new_arr = []
# for j in range(ceil(len_ls / 2)):
#     new_arr.append(a[j] * a[-j - 1])

# print(new_arr)























