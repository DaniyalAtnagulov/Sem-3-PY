# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

number = int(input('Enter fibonacci number: '))

fib = [0, 1]
nega_fib = [1]

for item in range(2, number+1):
    f = fib[item-2] + fib[item-1]
    fib.append(f)
    if item%2 == 0:
        nega_fib.insert(0, -(f))
    else:
        nega_fib.insert(0, f)

fin_fib = nega_fib + fib

print(f'{fin_fib}')