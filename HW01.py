# Задача 1. 
# Найдите сумму цифр трехзначного числа n.

# Результат сохраните в перменную res.

# n = 123

# res = n // 100 + n // 10 % 10 + n % 10

# print(f"Сумма цифр трёхзначного числа равно {res}") 

# Задача 2. 
# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали n журавликов.

# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# Выведите кортеж из количества журавликов, сделанных Петей, Катей и Сережей.

# n = 60

# sergey = n / 6
# petya = sergey
# katya = (sergey + petya) * 2
# print(int(sergey), int(katya), int(petya))

# Задача 3. Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.

# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.

# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.

# Вам требуется написать программу, которая проверяет счастливость билета с номером n и выводит на экран yes или no.

# n = 123456

# a = n // 100000
# b = n // 10000 % 10
# c = n // 1000 % 10
# d = n // 100 % 10
# e = n // 10 % 10
# f = n % 10

# sum1 = a + b + c
# sum2 = d + e + f

# if sum1 == sum2:
#   print("yes")
# else:
#   print("no")

# Задача 4. Определите, можно ли от шоколадки размером a × b долек отломить c долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# Выведите yes или no соответственно.
# a = 3
# b = 2
# c = 1

# if c % a == 0 or c % b == 0:
#     print("yes")
# else:
#     print("no")