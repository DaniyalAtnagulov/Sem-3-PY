# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def to_bin ():
    print("This is a binary number :", bin(int(input("'Input decimal number: ': ")))[2:])
to_bin()


# Если вариант с использованием встроенных функций неприемлим


num = int(input('Input decimal number: '))

def to_bin_2 (number):
    res = ''
    while number != 0:
        left = number % 2
        res = str(left) + res
        number //= 2
    print(f'This is a binary number: {res}')
to_bin_2 (num)