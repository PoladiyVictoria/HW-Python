# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. 
# Она растёт на круглой грядке, причём кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора 
# на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, 
# находясь перед некоторым кустом заданной во входном файле грядки.

n = int(input('Введите число N: '))
number_of_berries = []
sum_berries = []
import random
for _ in range(n):
    number_of_berries.append(random.randint(1, 101))
print(number_of_berries)
for i in range(len(number_of_berries)):
    sum = 0
    if i == n - 2:
        sum = number_of_berries[i] + number_of_berries[i + 1] + number_of_berries[0]
        sum_berries.append(sum)
    if i == n - 1:
        sum = number_of_berries[i] + number_of_berries[1] + number_of_berries[0]
        sum_berries.append(sum)
    if i < n - 2:
        sum = number_of_berries[i] + number_of_berries[i + 1] + number_of_berries[i + 2]
        sum_berries.append(sum)
max = sum_berries[0]
for i in range(len(sum_berries)):
    if sum_berries[i] > max:
        max = sum_berries[i]
print(f'Максимальное число ягод за один заход равно {max}')
