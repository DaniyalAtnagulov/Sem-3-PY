# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]



from math import ceil

def main():
    my_list=[]
    ml_l=int(input("enter len"))

    for item in range(ml_l):
        my_list.append (int(input(f'{item+1}')))
    print(my_list)

    new_list=[]
    for j in range(ceil(ml_l/2)):
        new_list.append(my_list[j]*my_list[-j-1])
    print(new_list)
main()


























