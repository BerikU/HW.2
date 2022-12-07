# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Без работы с методами строк.

n = Abs(float(input("Insert number ")))
sum_1 = 0

while n > 0:
    temp = n % 10
    sum_1 += temp
    n = n/10
print(sum_1)

# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N в виде списка.
#
# n = int(input())
# sum_1 = 1
# list_1 = []
#
# for i in range(1, n+1):
#     sum_1 *= i
#     list_1.append(sum_1)
# print(list_1)

# 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.

n = int(input("Insert number"))
list_1 = []
sum_1 = 0

sum_1 = (1+1/n)**n
list_1.append(sum_1)

print(list_1)