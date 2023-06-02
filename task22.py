# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

n = int(input('Введите число N: '))
m = int(input('Введите число M: '))
first_set = set()
second_set = set()
import random
for _ in range(n):
    first_set.add(random.randint(1, 30))
for _ in range(m):
    second_set.add(random.randint(1, 30))
print(first_set)
print(second_set)
first_set = first_set.intersection(second_set)
first_set = list(first_set)
first_set.sort()
print(first_set)
