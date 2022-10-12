/// Напишите функцию, которая вычисляет факториал натурального числа N.
print("Какое число в этот раз?")


n = int(input())

def factorial(n):
    pr = 1
    for i in range(2,n+1):
        pr=pr*i

    return pr

print(factorial(n))
