# Задайте список из n чисел последовательности  (1+1n)n  и выведите на экран их сумму.

n = int(input('Введите длину последовательности: '))
def sum_subsequence(n):
    sum_list = []
    my_sum = 0
    for i in range(1, n+1):
        my_sum = (1+1/i)**i
        sum_list.append(round(my_sum))
    return sum_list
print(f'Для n = {n}: {sum_subsequence(n)} -> {sum(sum_subsequence(n))}')