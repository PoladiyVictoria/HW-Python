# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no

m = int(input('Введите размер m шоколадки: '))
n = int(input('Введите размер n шоколадки: '))
k = int(input('Введите количество отломленных долек: '))
if k < m * n:
    if k >= m or k >= n:
        if k % m == 0 or k % n == 0:
            print("Введенное количество долек можно отломить")
        else:
           print("Введенное количество долек отломить нельзя")
    else:
        print("Введенное количество долек отломить нельзя") 
else:
    print("Введенное количество долек отломить нельзя") 


