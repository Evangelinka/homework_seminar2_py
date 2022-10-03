# Реализуйте алгоритм перемешивания списка.
# 1 способ
import random
n = int(input('Введите длину списка: '))
my_list = list(range(n))
print(my_list)
for i in my_list:
    temp = my_list[i]
    my_list.pop(i)
    my_list.append(temp)
print(my_list)

# 2 способ
n = int(input('Введите длину списка: '))
my_list = list(range(n))
print(my_list)
for i in range(len(my_list)-1, 0, -1):
    rand = random.randint(0, i+1)
    temp = my_list[i]
    my_list[i] = my_list[rand]
    my_list[rand] = temp
print(my_list)

# 3 способ
n = int(input('Введите длину списка: '))
my_list = list(range(n))
print(my_list)
my_list = list(set(my_list))
print(my_list)