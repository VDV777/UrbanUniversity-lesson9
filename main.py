# Дан список чисел [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
# Нужно выписывать из этого списка только положительные числа до тех пор, пока не встретите отрицательное или не закончится список (выход за границу).

# Пункты задачи:
# Запишите исходный список в переменную my_list.
# Напишите цикл while с соответствующими задаче условиями.
# Используйте операторы прерывания/продолжения цикла в соответствии с условиями задачи.

i = 0
while True:

    if i > my_list.__len__() - 1:
        break

    if my_list[i] >= 0:
        print(my_list[i])
    else:
        i += 1
        continue

    i += 1

