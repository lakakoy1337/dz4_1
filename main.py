// Создайте функцию, которая вычисляет сумму всех чисел от 1 до N. N — параметр функции.
print("Введи скок чисел надо:")
n = int(input())


def sum(n):
    summa = 0
    for i in range(1, n + 1):
        summa = summa + i
    return summa


print(sum(n))
