#       4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
#       Для решения используйте цикл while и арифметические операции.

num = int(input('Введите положительное число: '))
m = 1
while True:
    if num > 0:
        f = num % 10
        if f >= m:
            m = f
        else:
            m = m
        num = num // 10
    else:
        break
print('Максимальное значение цифры равно', m)

