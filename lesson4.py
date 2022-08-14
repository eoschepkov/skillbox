
def sum_factorials(num):
    part_factorial, summa = 1, 0

    for i in range(1, num + 1):
        part_factorial *= i
        summa += part_factorial
    return summa

n = int(input('Введите число: '))
print(sum_factorials(n))