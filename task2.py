# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

a = int(input('Введите трехзначное число: '))
if 100 <= a <= 999:
    sum = 0
    while a > 0:
        sum = sum + (a % 10)
        a = a // 10
    print(f'Сумма цифр равна {sum}')
else: 
    print('Введите трехзначное число!')
