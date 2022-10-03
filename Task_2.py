# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] 

n = int(input('Введите число N: '))
def prod_numbers(n):
  num_prod_list = []
  prod_num = 1
  for i in range(1, n+1):
    prod_num *= i
    num_prod_list.append(prod_num)
  return num_prod_list
print(f'Для числа от 1! до {n}! = {prod_numbers(n)}')