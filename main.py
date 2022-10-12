n = int(input("Введите число: "))
def counter(n):
    count = 0
    while n > 0:
        n = n // 10
        count = count + 1
    return (count)

print("Количество цифр в числе:", counter(n))
