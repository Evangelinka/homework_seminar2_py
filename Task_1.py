# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23

number = input('Введите вещественное число: ')
def sum_digits(number):
  sum_dig = 0
  for i in (number):
    if i != '.':
      sum_dig += int(i)
  return sum_dig
print(f'Сумма цифр в числе {number} = {sum_digits(number)}')