#   3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь
#   ввёл число 3. Считаем 3 + 33 + 333 = 369.

num_mono = str(input('введите число от 1 до 9: '))
num_duo = num_mono + num_mono
num_trio = num_mono + num_duo
print('a=', num_mono)
print('aa=', num_duo)
print('aaa=', num_trio)
rez = int(num_mono) + int(num_duo) + int(num_trio)
print('a + aa + aaa =', rez)