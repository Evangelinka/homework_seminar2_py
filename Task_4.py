# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

n = int(input('Введите число N: '))
number_list = list(range(-n, n+1))
path = 'file.txt'
data = open(path, 'r')
my_prod = 1
for line in data:
    my_prod = number_list[int(line)] * my_prod
data.close()
print(f'Список от -{n} до {n}: {number_list}')
print(f'Произведение чисел из файла: {my_prod}')